Summary: Adobe Acrobat
Name: acrobat
Version: 3.0
Release: 2
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar

%description
Adobe Acrobat is typesetting software.

%prep
%setup -q

%install
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

cd $build_dir/files
find . -print | cpio -pdmuv $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/man/manl/*
/usr/local/bin/*
/opt/Acrobat3
