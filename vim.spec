%include gnome-header.spec

Name: vim
Version: 5.8
Copyright: Charityware
Group: Applications/Editors
Summary: VI iMproved
Release: 2
Source0: vim-%{version}-src.tar.gz
Source1: vim-%{version}-rt.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: %{gtk_pkg}
BuildRequires: %{gtk_dev}
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
%setup -q
%setup -q -D -T -b 1

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib %{gnome_ldflags}" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib %{gnome_ldflags}" \
 CPPFLAGS="-I/usr/local/include" ./configure --prefix=/usr/local \
 --enable-gui=gtk --with-gtk-prefix=%{gtk_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/doc
make install prefix=$RPM_BUILD_ROOT/usr/local
ln -s ../share/vim/vim58 $RPM_BUILD_ROOT/usr/local/doc/vim-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/share/vim/vim58
/usr/local/man/man1/*
/usr/local/doc/vim-%{version}
