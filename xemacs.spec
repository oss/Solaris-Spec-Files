#Depricated/EOL package
IgnoreOS: Solaris

Summary: Emacs, with more features
Name: xemacs
Version: 21.4.3
Release: 4
Group: Applications/Editors
Copyright: GPL
Source0: xemacs-%{version}.tar.gz
Source1: xemacs-%{version}-elc.tar.gz
Source2: xemacs-%{version}-info.tar.gz
Source3: xemacs-sumo.tar.gz
Source4: xemacs-mule-sumo.tar.gz
BuildRequires: libpng libjpeg libungif-devel tiff xpm
Requires: libpng libjpeg libungif tiff xpm
BuildRoot: /var/tmp/%{name}-root
Conflicts: vpkg-SFWxmacs

%description
XEmacs is a highly customizable open source text editor and
application development system. It is protected under the GNU Public
License and related to other versions of Emacs, in particular GNU
Emacs. Its emphasis is on modern graphical user interface support and
an open software development model, similar to Linux. XEmacs has an
active development community numbering in the hundreds, and runs on
Windows 95 and NT, Linux and nearly every other version of Unix in
existence. Support for XEmacs has been supplied by Sun Microsystems,
University of Illinois, Lucid, ETL/Electrotechnical Laboratory, Amdahl
Corporation, BeOpen, and others, as well as the unpaid time of a great
number of individual developers.

%package ctags
Summary: Xemacs ctags
Group: Applications/Editors

%description ctags
Xemacs-ctags is a program that helps you browse C source code.

%package b2m
Summary: Xemacs babyl to mbox
Group: Applications/Editors

%description b2m
Xemacs-b2m lets you convert your babyl-format mailbox into a regular
unix mailbox.

%prep
%setup -q
%setup -q -D -T -b 1
%setup -q -D -T -b 2
%setup -q -D -T -a 3
%setup -q -D -T -a 4

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local --with-mule --without-ldap
make

%install
umask 022
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/xemacs
make install prefix=$RPM_BUILD_ROOT/usr/local
find xemacs-packages | cpio -pdm $RPM_BUILD_ROOT/usr/local/lib/xemacs
find mule-packages | cpio -pdm $RPM_BUILD_ROOT/usr/local/lib/xemacs

%clean
rm -rf $RPM_BUILD_ROOT

%files ctags
%defattr(-,bin,bin)
/usr/local/bin/etags
/usr/local/bin/ctags
/usr/local/man/man1/etags.1
/usr/local/man/man1/ctags.1

%files b2m
%defattr(-,bin,bin)
/usr/local/bin/b2m

%files
%defattr(-,bin,bin)
/usr/local/bin/gnuclient
/usr/local/bin/ootags
/usr/local/bin/rcs-checkin
/usr/local/bin/gnudoit
/usr/local/bin/gnuattach
/usr/local/bin/xemacs-%{version}
/usr/local/bin/xemacs
/usr/local/bin/ellcc
/usr/local/man/man1/xemacs.1
/usr/local/man/man1/gnuserv.1
/usr/local/man/man1/gnuclient.1
/usr/local/man/man1/gnuattach.1
/usr/local/man/man1/gnudoit.1
/usr/local/lib/xemacs-%{version}
/usr/local/lib/xemacs
