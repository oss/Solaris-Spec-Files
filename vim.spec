
%define name vim
%define version 7.1
%define vim_version 71
%define release 1
%define prefix /usr/local

Name:		%{name}
Version:	%{version}
Copyright:	Charityware
Group:		Applications/Editors
Summary:	VI iMproved
Release:	%{release}
Source:		%{name}-%{version}.tar.bz2
URL:		ftp://ftp.vim.org/pub/vim/unix/%{name}-%{version}.tar.bz2
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
#Requires:	gtk2
#BuildRequires:	gtk2-devel
Conflicts:	vpkg-SFWvim

%description
Vim is an almost compatible version of the UNIX editor Vi.  Many new features
have been added: multi level undo, syntax highlighting, command line history,
on-line help, filename completion, block operations, etc.  There is also a
Graphical User Interface (GUI) available.  See doc/vi_diff.txt.

This editor is very useful for editing programs and other plain ASCII files.
All commands are given with normal keyboard characters, so those who can type
with ten fingers can work very fast.  Additionally, function keys can be
defined by the user, and the mouse can be used.


%prep
%setup -q -n %{name}%{vim_version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/include/ncursesw" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix="/usr/local" \
	--enable-gui="no" \
	--with-compiledby=dhalik \
	--with-feature="normal" \
	--disable-darwin \
	--disable-netbeans \
	--disable-gtktest

gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/doc

gmake install prefix=$RPM_BUILD_ROOT/usr/local

ln -s ../share/%{name}/%{name}%{vim_version} $RPM_BUILD_ROOT/usr/local/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
/usr/local/bin/*
/usr/local/share/%{name}/%{name}%{vim_version}
/usr/local/man/*
/usr/local/doc/%{name}-%{version}

%changelog
* Tue May 15 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 7.1-1
- Bumped to 7.1
- Removed GTK support

