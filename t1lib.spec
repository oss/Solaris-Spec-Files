%define t1lib_ver 5.1.0
%define source_file t1lib-%{t1lib_ver}.tar.gz
%define prefix /usr/local

Name: t1lib
Version: %{t1lib_ver}
Copyright: LGPL
Release: 2
Summary: A font rendering library
Group: X11/Libraries 
Source: %{source_file}
BuildRoot: %{_tmppath}/%{name}-root
Provides: t1lib

%description
t1lib is a library distributed under the GNU General Public Library
License for generating character- and string-glyphs from Adobe Type 1
fonts under UNIX. t1lib uses most of the code of the X11 rasterizer
donated by IBM to the X11-project.


%prep
%setup -q

%build
CC="cc"
CXX="CC"
CPPFLAGS="-I/usr/local/include/freetype2 -I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export CC CXX CPPFLAGS LD LDFLAGS
./configure --prefix=%{prefix}  
#people need to learn how to write Makefiles
CURRENTDIR=`pwd`
cd $RPM_BUILD_DIR/t1lib-%{t1lib_ver}/type1afm
mv Makefile Makefile.wrong
sed -e 's/$(INSTALL_PROGRAM) type1afm $(bindir)\/type1afm/$(INSTALL_PROGRAM) type1afm $(DESTDIR)$(bindir)\/type1af/' Makefile.wrong > Makefile
cd $CURRENTDIR
make without_doc

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} 



%clean
[ %{buildroot} != "/" ] && [ -d %{buildroot} ] && rm -rf %{buildroot}

%post

%files
%defattr(-, root, root)
%{prefix}/lib
%{prefix}/include
%{prefix}/share
%{prefix}/share/t1lib
%{prefix}/bin


