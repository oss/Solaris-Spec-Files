Name: vim
Version: 7.0
Copyright: Charityware
Group: Applications/Editors
Summary: VI iMproved
Release: 4
Source0: vim-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: gtk2
BuildRequires: gtk2-devel
Conflicts: vpkg-SFWvim

%description
Vim is an almost compatible version of the UNIX editor Vi.  Many new features
have been added: multi level undo, syntax highlighting, command line history,
on-line help, filename completion, block operations, etc.  There is also a
Graphical User Interface (GUI) available.  See doc/vi_diff.txt.

This editor is very useful for editing programs and other plain ASCII files.
All commands are given with normal keyboard characters, so those who can type
with ten fingers can work very fast.  Additionally, function keys can be
defined by the user, and the mouse can be used.

     [from README.txt]

%prep
%setup -q -n vim70

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/include/ncursesw" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --enable-gui=gtk2 --with-compiledby=leozh --with-feature=huge
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/doc

gmake install prefix=$RPM_BUILD_ROOT/usr/local

ln -s ../share/vim/vim70 $RPM_BUILD_ROOT/usr/local/doc/vim-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
/usr/local/bin/*
/usr/local/share/vim/vim70
/usr/local/man/*
/usr/local/doc/vim-%{version}

