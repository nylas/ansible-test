FROM gentoo/stage3-amd64

MAINTAINER SJLC

ADD http://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2 /


RUN mkdir -p /usr
RUN bzcat /portage-latest.tar.bz2 | tar -xf - -C /usr
RUN mkdir -p /usr/portage/distfiles /usr/portage/metadata /usr/portage/packages

VOLUME /usr/portage
