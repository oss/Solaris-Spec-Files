# I would really like to replace this (as well as ru-pam and ru-rsh)
# with a proper RPM, built from source.

Summary: RDIST replacement
Name: ru-rdist
Version: 1.0
Release: 3
Group: System Environment/Base
Copyright: Rutgers
Source: ru-rdist.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
The utility rdist maintains copies of files on multiple hosts. It
preserves the owner, group, mode, and modification time of the master
copies, and can update programs that are executing

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
ln -s usr/bin/rdist usr/ucb/rdist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/ucb/*
/usr/bin/rdist
/usr/local/man/man1/*
/usr/local/man/man4/*

