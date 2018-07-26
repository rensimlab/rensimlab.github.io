def sync():
    import os
    from bson.objectid import ObjectId
    from girder import logger
    from girder.models.assetstore import Assetstore
    from girder.models.collection import Collection
    from girder.models.file import File
    from girder.models.folder import Folder
    from girder.models.item import Item
    from girder.models.user import User
    from girder.exceptions import ResourcePathNotFound
    from girder.utility import path as path_utils
    from girder.utility import assetstore_utilities

    assetstoreId = ObjectId('59b04a2c38eed90001dcc45c')
    assetstore = Assetstore().load(id=assetstoreId)
    adapter = assetstore_utilities.getAssetstoreAdapter(assetstore)

    physicalPath = '/mnt/data/renaissance'
    collectionPath = '/collection/Renaissance Simulations'
    collectionId = ObjectId('59b04a0e38eed90001dcc45b')
    rslCollection = Collection().load(collectionId, force=True)
    admin = list(User().getAdmins())[0]

    def purge_leaf_folder(path):
        folder = path_utils.lookUpPath(path, user=admin)['document']
        if Item().find({'folderId': folder['_id']}).count() > 0 or \
                list(Folder().childFolders(folder, 'folder', user=admin)):
            return
        logger.info("Removing empty folder %s" % path)
        Folder().remove(folder)
        purge_leaf_folder(os.path.dirname(path))

    q = {'assetstoreId': assetstoreId, 'imported': True}
    fields = ['path', 'size', 'name', 'mtime']

    girderFiles = {
        fObj.pop('path'): fObj for fObj in File().find(q, fields=fields)
    }

    toImport = {}
    toModify = {}

    for (dirpath, dirnames, filenames) in os.walk(physicalPath):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            stat = os.stat(path)

            try:
                girderObj = girderFiles.pop(path)
            except KeyError:
                toImport[path] = {
                    'mtime': stat.st_mtime, 'size': stat.st_size,
                    'name': filename
                }

            if girderObj['mtime'] != stat.st_mtime or \
                    girderObj['size'] != stat.st_size or \
                    girderObj['name'] != filename:
                girderObj.update({
                    'mtime': stat.st_mtime, 'size': stat.st_size,
                    'name': filename, 'path': path
                })
                toModify[girderObj.pop('_id')] = girderObj

    # Remove orphaned files
    potentialLeafFolders = set()
    for orphan in girderFiles.values():
        fileObj = File().load(ObjectId(orphan['_id']), force=True)
        itemObj = Item().load(fileObj['itemId'], force=True)
        File().remove(fileObj)
        girderPath = path_utils.getResourcePath('item', itemObj, force=True)
        if not list(Item().childFiles(itemObj)):
            Item().remove(itemObj)
            potentialLeafFolders.add(os.path.dirname(girderPath))
        logger.info('Removed %s' % girderPath)

    # Remove empty folders
    for path in list(potentialLeafFolders):
        purge_leaf_folder(path)

    # Import new items
    for filePath, newFile in toImport.items():
        relpath = os.path.relpath(filePath, physicalPath)
        parentType = 'collection'
        parent = rslCollection

        dirs = os.path.dirname(relpath).split('/')
        for directory in dirs:
            try:
                parent, parentType = \
                    path_utils.lookUpToken(directory, parentType, parent)
            except ResourcePathNotFound:
                parent = Folder().createFolder(
                    parent, directory, parentType=parentType,
                    public=True, creator=admin)
                parentType = 'folder'

        adapter._importDataAsItem(
            os.path.basename(relpath), admin, parent,
            os.path.dirname(filePath), [os.path.basename(filePath)],
            reuseExisting=True)
        logger.info('Imported %s to %s' %
              (filePath, os.path.join(collectionPath, relpath)))
