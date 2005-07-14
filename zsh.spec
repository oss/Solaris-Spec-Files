Name: zsh
Version: 4.2.5
Copyright: BSD type
Group: System Environment/Shells
Summary: the Z shell
Release: 1
Source0: zsh-%{version}.tar.bz2
Source1: zsh-%{version}-doc.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root
Vendor: NBCS-OSS
Packager: Hardik Varia <hvaria@nbcs.rutgers.edu>
%description
Zsh is a powerful shell with elements of ksh, csh, bash, and more.
Install this package if you want to use zsh.  You also may want to
install zsh-doc.


%package doc
Summary: Z shell docs
Group: Documentation

%description doc
zsh-doc contains info, ps, and html documentation for zsh.  You
probably should install this package if you have zsh installed.

%prep
%setup -q
%setup -T -D -b 1

%build
./configure --prefix=/usr/local --with-tcsetpgrp
make


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/info
cp Doc/zsh.info* %{buildroot}/usr/local/info
make install prefix=%{buildroot}/usr/local

cd %{buildroot}/usr/local
/usr/local/bin/unhardlinkify.py ./

%post
cat << EOF

After you install this package, add /usr/local/bin/zsh  to /etc/shells.

EOF

%post doc
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir="/usr/local/info" \
    --entry="* zsh: (zsh).                The Z shell" \
    /usr/local/info/zsh.info
fi

%preun doc
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir="/usr/local/info" \
    --delete /usr/local/info/zsh.info
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/bin/*
/usr/local/lib/zsh/%{version}
/usr/local/share/zsh/%{version}
/usr/local/share/zsh/site-functions
/usr/local/man/man1/*

%files doc
%defattr(-, root, bin)
%doc Doc/*ps README Doc/*html Doc/*dvi
/usr/local/info/zsh.info*

%changelog
* Wed Jul 13 2005 Hardik Varia <hvaria@nbcs.rutgers.edu>
- Updated to 4.2.5
* Mon Jun 27 2005 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
- Updated to 4.2.1
* Wed Dec 19 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Removed inaccurate "Conflicts:" line
