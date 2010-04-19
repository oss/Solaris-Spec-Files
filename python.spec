%define pybasever 2.6 

Summary:       The Python language interpeter
Name:          python
Version:       2.6.4
Release:       9
Group:         Development/Languages
License:       Python
URL:           http://www.python.org/
Source:        http://www.python.org/ftp/python/%{version}/Python-%{version}.tgz
# Solaris specific config options
Patch0:        python-2.6.4-config-solaris.patch
# To build against db4-4.8
Patch1:        python-2.6-update-bsddb3-4.8.patch
# Undefine gethostname() as it is already defined in /usr/include/unistd.h
Patch2:        python-2.6-undef-gethostname.patch
# make os.mknod() available on solaris. See:
# http://bugs.python.org/issue3928
Patch3:        python-enable-mknod-solaris.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:      tcl-tk, tcl, readline5, gdbm, gmp, ncurses, sqlite, expat, openssl
BuildRequires: tcl, tcl-tk, readline5-devel, gdbm, gmp-devel, ncurses-devel, sqlite-devel, expat-devel, openssl
BuildRequires: db4-devel >= 4.8

%description
Python is an interpreted, object-oriented, high-level programming
language with dynamic semantics.  Its high-level built in data
structures, combined with dynamic typing and dynamic binding, make it
very attractive for rapid application development, as well as for use
as a scripting or glue language to connect existing components
together.  Python's simple, easy to learn syntax emphasizes
readability and therefore reduces the cost of program maintenance.
Python supports modules and packages, which encourages program
modularity and code reuse.  The Python interpreter and the extensive
standard library are available in source or binary form without charge
for all major platforms, and can be freely distributed.

%prep
%setup -q -n Python-%{version}
%patch0 -p1 
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Our compiler doesn't like this flag
sed -i '/OPT:Olimit=0/d' configure

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc -mt" CXX="CC -mt" CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include/ncursesw -I/usr/local/include/readline -I/usr/local/include/db4 -I/usr/local/include -fPIC" \
CFLAGS="-I/usr/local/ssl/include -I/usr/local/include/ncursesw -I/usr/local/include/readline -I/usr/local/include/db4 -I/usr/local/include -fPIC" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib -L/usr/lib -R/usr/lib -lc -lncursesw -Bdirect" \
LD_PRELOAD="/usr/local/ssl/lib/libcrypto.so" \
LANG="C"
export PATH CC CXX CFLAGS CPPFLAGS LD LDFLAGS LD_PRELOAD LANG


cp Modules/Setup.dist Modules/Setup

SSL=/usr/local/ssl
export SSL
EXPAT_DIR=/usr/local
export EXPAT_DIR
cat << EOF >> Modules/Setup
_curses _cursesmodule.c -lncursesw
_curses_panel _curses_panel.c -lpanel -lncursesw

readline readline.c -lreadline -lncursesw -I/usr/local/include/readline -L/usr/local/lib

_socket socketmodule.c


_ssl _ssl.c \
       -DUSE_SSL -I$SSL/include -I$SSL/include/openssl \
       -L$SSL/lib -lssl -lcrypto

crypt cryptmodule.c # -lcrypt  # crypt(3); needs -lcrypt on some systems

sunaudiodev sunaudiodev.c

_tkinter _tkinter.c tkappinit.c -DWITH_APPINIT \
       -L/usr/local/lib \
       -I/usr/local/include \
       -I/usr/openwin/include \
       -ltk8.4 -ltcl8.4 \
       -L/usr/openwin/lib \
       -lX11

gdbm gdbmmodule.c -I/usr/local/include -L/usr/local/lib -lgdbm

cStringIO cStringIO.c
cPickle cPickle.c

fpectl fpectlmodule.c -R/opt/SUNWspro/lib -lsunmath -lm


pyexpat pyexpat.c -DHAVE_EXPAT_H -I$EXPAT_DIR/lib -L$EXPAT_DIR -lexpat

EOF

./configure --with-threads --prefix=/usr/local --without-gcc --enable-shared

#sed -e 's/-I. -I$(srcdir)\/Include/-I. -I$(srcdir)\/Include -I\/usr\/local\/include\/db4 -I\/usr\/local\/include -I\/usr\/local\/include\/ncursesw -I\/usr\/local\/include\/readline/g' -i Makefile

gmake BLDSHARED="cc -mt -G -L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib" %{?_smp_mflags} 

topdir=%{_builddir}/Python-%{version}
# Shebangs should point to the newly built python:
LD_LIBRARY_PATH=$topdir $topdir/python Tools/scripts/pathfix.py -i "%{_bindir}/env python%{pybasever}" .

# Rebuild with new python
# We need a link to a versioned python in the build directory
ln -s python python%{pybasever}

rm -rf libpython2.6.so
LD_LIBRARY_PATH=$topdir PATH=$PATH:$topdir gmake BLDSHARED="cc -mt -G -L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib -L/usr/lib -R/usr/lib -lc -Bdirect" -s OPT="$CFLAGS" ASDLGEN="$topdir/python Parser/asdl_c.py" %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

#Remove backups written by the pathfix.py script
find . -name "*~" -type f -exec rm -f {} \;

gmake install DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
topdir=%{_builddir}/Python-%{version}
LD_LIBRARY_PATH=$topdir $topdir/python /usr/local/bin/unhardlinkify.py .


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc LICENSE README Misc/*
/usr/local/share/man/man1/python.1
/usr/local/include/python*
/usr/local/lib/python*
/usr/local/lib/libpython*
/usr/local/bin/*

%changelog
* Fri Apr 16 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> 2.6.4-9
- Enable os.mknod() on Solaris
* Mon Feb 01 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> 2.6.4-8
- Comment out the workaround for defining gethostname() function in pyport.h
  Solaris already defines this in /usr/include/unistd.h 
* Fri Jan 29 2010 Orcan Ogenbil <orcan@nbcs.rutgers.edu> 2.6.4-7
- Make sure pathfix.py's backup files don't end up in the final package
* Thu Jan 28 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> 2.6.4-6
- Rebuild without gettext linkage
* Thu Jan 21 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> 2.6.4-5
- Add the necessary patch for db4 compatibility
* Fri Jan 08 2010 Russ Frank <rfranknj@nbcs.rutgers.edu> 2.6.4-4
- Respin against BDB4.8
* Wed Dec 02 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> 2.6.4-3
- Fix some broken links
* Wed Dec 02 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> 2.6.4-2
- I will not publish unsigned packages again
* Fri Nov 20 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> 2.6.4-1
- Update to 2.6.4
* Mon Oct 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.6-1
- Updated to version 2.6, removed db/db4 requirements
* Wed Jun 18 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.2-1
- Updated to version 2.5.2
* Wed Jan 31 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.5-2
- Updated to 2.5

