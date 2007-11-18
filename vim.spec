
%define name vim
%define version 7.1
%define vim_version 71
%define release 3
%define prefix /usr/local

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
Packager:       David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:  gtk2, gtk2-devel, ncurses-devel
Requires:	ncurses
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
Requires:       %{name} = %{version}, gtk2
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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/include/ncursesw" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
        --prefix="/usr/local" \
        --enable-gui="gtk2" \
        --with-compiledby="dhalik" \
        --with-feature="huge" \
        --disable-darwin \
	--with-x \
	--enable-gtk2-check \
	--disable-nls

gmake -j3

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/doc
gmake install prefix=$RPM_BUILD_ROOT/usr/local

rm -rf gvim
mkdir -p gvim/usr/local/bin

rm -rf $RPM_BUILD_ROOT%{_bindir}/evim
rm -rf $RPM_BUILD_ROOT%{_bindir}/eview
rm -rf $RPM_BUILD_ROOT%{_bindir}/gview
rm -rf $RPM_BUILD_ROOT%{_bindir}/gvimdiff
rm -rf $RPM_BUILD_ROOT%{_bindir}/rgview
rm -rf $RPM_BUILD_ROOT%{_bindir}/rgvim
rm -rf $RPM_BUILD_ROOT%{_bindir}/gvim

cp $RPM_BUILD_ROOT%{_bindir}/vim $RPM_BUILD_ROOT%{_bindir}/gvim

rm -rf $RPM_BUILD_ROOT%{_bindir}/vim

gmake clean

./configure \
	--prefix="/usr/local" \
	--enable-gui="no" \
	--with-compiledby="dhalik" \
	--with-feature="normal" \
	--disable-darwin \
	--disable-netbeans \
	--disable-gtktest \
	--disable-nls

gmake -j3

%install
#rm -rf $RPM_BUILD_ROOT
#mkdir -p $RPM_BUILD_ROOT/usr/local/doc

gmake install prefix=$RPM_BUILD_ROOT/usr/local

ln -s ../share/%{name}/%{name}%{vim_version} $RPM_BUILD_ROOT/usr/local/doc/%{name}-%{version}

cd $RPM_BUILD_ROOT/usr/local/bin

ln -s gvim evim
ln -s gvim eview
ln -s gvim gview
ln -s gvim gvimdiff
ln -s gvim rgview
ln -s gvim rgvim


%clean
rm -rf $RPM_BUILD_ROOT

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
%{_datadir}/%{name}/%{name}%{vim_version}
%{_mandir}/man1/vim.1
%{_mandir}/man1/vimdiff.1
%{_mandir}/man1/vimtutor.1
%{_mandir}/man1/xxd.1
%{_mandir}/man1/ex.1
%{_mandir}/man1/rview.1
%{_mandir}/man1/rvim.1
%{_mandir}/man1/view.1
%{_mandir}/man1/vim.1
%{_mandir}/man1/vimdiff.1
%{_mandir}/man1/vimtutor.1
%{_mandir}/man1/xxd.1
%{_docdir}/%{name}-%{version}

%files gtk
%defattr(-,root,bin)
%{_bindir}/eview
%{_bindir}/evim
%{_bindir}/gview
%{_bindir}/gvim
%{_bindir}/gvimdiff
%{_bindir}/rgview
%{_bindir}/rgvim
%{_mandir}/man1/evim.1
%{_mandir}/man1/eview.1
%{_mandir}/man1/evim.1
%{_mandir}/man1/gview.1
%{_mandir}/man1/gvim.1
%{_mandir}/man1/gvimdiff.1
%{_mandir}/man1/rgview.1
%{_mandir}/man1/rgvim.1

%changelog
* Tue May 15 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 7.1-2
- Seperated vim-gtk out of vim
* Tue May 15 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 7.1-1
- Bumped to 7.1
- Removed GTK support

