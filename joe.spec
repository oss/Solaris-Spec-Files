Name: joe
Version: 2.9.8
Release: 0
Summary: Simple mode-less editor
Source: joe-%{version}.tar.gz
Copyright: GPL
Group: Applications/Editors
BuildRoot: /var/tmp/%{name}-root

%description
JOE  is  a  powerful  ASCII-text  screen editor.  It has a "mode-less" user interface which is similer to many  user-friendly  PC  editors.   Users  of Micro-Pro's WordStar or Borland's "Turbo" languages will feel at home.  JOE  is  a full featured UNIX screen-editor though, and has many features for editing programs and text.
%prep
%setup -q

%build
./configure --prefix=/usr/local --exec-prefix=/usr/local 
--bindir=$(RPM_BUILD_ROOT)/usr/local/bin --mandir=$(RPM_BUILD_ROOT_/usr/local//man
make

%install
PREFIX="%{buildroot}"
EPREFIX="%{buildroot}"
export PREFIX EPREFIX

make install prefix=/tmp/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/*
