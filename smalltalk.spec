Summary: Gnu Smalltalk environment
Name: smalltalk
Version: 1.8.3
Release: 2
Group: Development/Languages
URL: http://www.smalltalk.org/
Copyright: GPL
Source: smalltalk-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: readline
Requires: tcl >= 8.3.1, tcl-tk
Requires: libtool
BuildRequires: autoconf

%description
Smalltalk is an object-oriented language developed at the Xerox PARC.
The GNU implementation closely follows the Smalltalk-80 language and
is good for rapid prototyping.

%prep
%setup -q

%build
aclocal --acdir=m4
autoconf
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure
make

%install
rm -rf $RPM_BUILD_ROOT

umask 022

for i in bin lib info include man/man1; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done

for i in kernel blox examples examples/gdbm examples/blox examples/mixed tcp \
         cint compiler test xml ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/share/gnu-smalltalk/$i
done

install -c -m 755 gst $RPM_BUILD_ROOT/usr/local/bin/gst
install -c -m 755 gst-config $RPM_BUILD_ROOT/usr/local/bin/gst-config
install -c -m 755 gst-package $RPM_BUILD_ROOT/usr/local/bin/gst-package
install -c -m 644 lib/gst.h $RPM_BUILD_ROOT/usr/local/include/gst.h
install -c -m 644 lib/gstpub.h $RPM_BUILD_ROOT/usr/local/include/gstpub.h
install -c -m 644 gstconf.h $RPM_BUILD_ROOT/usr/local/include/gstconf.h
install -c -m 644 lib/libgst.a $RPM_BUILD_ROOT/usr/local/lib/libgst.a
install -c -m 644 docs/gst.1 $RPM_BUILD_ROOT/usr/local/man/man1/gst.1

for i in `ls docs/gst.info* | sed 's/^docs\///`; do
   install -c -m 644 docs/$i $RPM_BUILD_ROOT/usr/local/info/$i;
done

TMP_FILE_LIST=`find . \( -name \*.st -o -name \*.ok -o -name README \
    -o -name \*.gif -o -name \*.txt \) -print | sed 's/^\.\///'`
EXTRA_FILE_LIST="packages test/do-check examples/mixed/binary.c \
    examples/shell"
for i in $TMP_FILE_LIST $EXTRA_FILE_LIST ; do
    install -c -m 644 $i \
        $RPM_BUILD_ROOT/usr/local/share/gnu-smalltalk/$i
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
x=`pwd`; cd /usr/local/share/gnu-smalltalk && $x/gst dummyFile -Vi
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir=/usr/local/info \
      /usr/local/info/gst.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir=/usr/local/info --delete \
      /usr/local/info/gst.info
fi

%files
%defattr(-,bin,bin)
%doc COPYING* NEWS AUTHORS README
/usr/local/bin/*
/usr/local/include/*
/usr/local/man/man1/*
/usr/local/lib/*
/usr/local/info/*
/usr/local/share/gnu-smalltalk
