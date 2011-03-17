%define name vim
%define version 7.3
%define vim_version 73
%define release 1

Name:		%{name}
Version:	%{version}
License:	Charityware
Group:		Applications/Editors
Summary:	VI iMproved
Release:	%{release}
Source:		%{name}-%{version}.tar.bz2
URL:		ftp://ftp.vim.org/pub/vim/unix/%{name}-%{version}.tar.bz2
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Phillip Quiza <pquiza@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:  gtk2-devel, ncurses-devel
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

%package gtk
Summary:        VI iMproved GTK
Group:          Applications/Editors
Requires:       %{name} = %{version}-%{release}, gtk2
Conflicts:      vpkg-SFWvim

%description gtk
VIM-GTK is a version of the VIM editor which will run within the
X Window System.  If you install this package, you can run VIM as an X
application with a full GUI interface and mouse support.

Install the vim-gtk package if you'd like to try out a version of vi
with graphics and mouse capabilities.  You'll also need to install the
vim base package.

%prep
%setup -q -n %{name}%{vim_version}


%build
CPPFLAGS="-I/usr/local/include/ncursesw"
CFLAGS="-I/usr/local/include/ncursesw"
export CFLAGS CPPFLAGS

%configure \
        --enable-gui="gtk2" \
        --with-compiledby="orcan" \
        --disable-darwin \
	--with-x \
	--enable-gtk2-check \
	--disable-nls

gmake -j3

rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_bindir}/evim
rm -f %{buildroot}%{_bindir}/eview
rm -f %{buildroot}%{_bindir}/gview
rm -f %{buildroot}%{_bindir}/gvimdiff
rm -f %{buildroot}%{_bindir}/rgview
rm -f %{buildroot}%{_bindir}/rgvim
rm -f %{buildroot}%{_bindir}/gvim

mv %{buildroot}%{_bindir}/vim %{buildroot}%{_bindir}/gvim

gmake clean

unset CFLAGS CPPFLAGS LDFLAGS
CPPFLAGS="-I/usr/local/include/ncursesw"
CFLAGS="-I/usr/local/include/ncursesw"
export CFLAGS CPPFLAGS

%configure \
	--enable-gui="no" \
	--with-compiledby="orcan" \
	--disable-darwin \
	--disable-netbeans \
	--disable-gtktest \
	--disable-nls

gmake -j3

%install
gmake install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/usr/local/doc
ln -s ../share/%{name}/%{name}%{vim_version} %{buildroot}/usr/local/doc/%{name}-%{version}

cd %{buildroot}%{_bindir}

ln -s gvim evim
ln -s gvim eview
ln -s gvim gview
ln -s gvim gvimdiff
ln -s gvim rgview
ln -s gvim rgvim

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%{_bindir}/ex
%{_bindir}/rview
%{_bindir}/rvim
%{_bindir}/view
%{_bindir}/vim
%{_bindir}/vimdiff
%{_bindir}/vimtutor
%{_bindir}/xxd
%{_mandir}/man1/vim.1
%{_mandir}/man1/vimdiff.1
%{_mandir}/man1/vimtutor.1
%{_mandir}/man1/xxd.1
%{_mandir}/man1/ex.1
%{_mandir}/man1/rview.1
%{_mandir}/man1/rvim.1
%{_mandir}/man1/view.1
%docdir %{_datadir}/%{name}/%{name}%{vim_version}
%{_datadir}/%{name}/%{name}%{vim_version}
/usr/local/doc/%{name}-%{version}

%files gtk
%defattr(-,root,bin)
%{_bindir}/eview
%{_bindir}/evim
%{_bindir}/gview
%{_bindir}/gvim
%{_bindir}/gvimtutor
%{_bindir}/gvimdiff
%{_bindir}/rgview
%{_bindir}/rgvim
%{_mandir}/man1/evim.1
%{_mandir}/man1/eview.1
%{_mandir}/man1/gview.1
%{_mandir}/man1/gvim.1
%{_mandir}/man1/gvimdiff.1
%{_mandir}/man1/rgview.1
%{_mandir}/man1/rgvim.1

%changelog
* Thu Mar 17 2011 Phillip Quiza <pquiza@nbcs.rutgers.edu> - 7.3-1
- Bumped to 7.3
* Thu Aug 19 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 7.2-2
- Backport official patch 7.2.257 to get rid of assertion failed warnings
* Fri Aug 15 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.2-1
- Cleaned up the spec file somewhat, added %docdir directive, bumped to 7.2
* Tue May 15 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 7.1-2
- Seperated vim-gtk out of vim
* Tue May 15 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 7.1-1
- Bumped to 7.1
- Removed GTK support

