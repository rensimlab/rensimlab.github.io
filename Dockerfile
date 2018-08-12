FROM starefossen/ruby-node:2-6-alpine

ENV GITHUB_GEM_VERSION 190

RUN apk --update add --virtual build_deps \
    build-base ruby-dev libc-dev linux-headers \
  && gem install --no-document \
    github-pages:${GITHUB_GEM_VERSION} \
    jekyll-github-metadata \
    jekyll-feed \
    jekyll-theme-midnight \
    jekyll-youtube \
    minima \
    minitest \
    tzinfo-data \
  && apk del build_deps \
  && apk add git \
  && mkdir -p /usr/src/app \
  && rm -rf /usr/lib/ruby/gems/*/cache/*.gem

WORKDIR /usr/src/app

EXPOSE 4000
COPY . /usr/src/app
CMD jekyll serve -d /_site --watch --force_polling -H 0.0.0.0 -P 4000
