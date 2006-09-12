%define xpdf_ver 3.01
%define source_file xpdf-%{xpdf_ver}.tar.gz
%define prefix /usr/local

Name: xpdf
Version: %{xpdf_ver}
Copyright: GPL V2 
Release: 3
Summary: A light weight PDF viewer
Group: Applications/Viewers
Source: %{source_file}
Patch0: xpdf-3.01pl2.patch
Patch1: 05_freetype-2.2.dpatch
Requires: freetype2 >= 2.0.5
BuildRequires: freetype2-devel >= 2.0.5 t1lib sed
BuildRoot: %{_tmppath}/%{name}-root
Provides: xpdf

%description
Xpdf is an open source viewer for Portable Document Format (PDF)
files.  (These are also sometimes also called 'Acrobat' files, from
the name of Adobe's PDF software.)  The Xpdf project also includes a
PDF text extractor, PDF-to-PostScript converter, and various other
utilities.

To run xpdf, simply type:
  xpdf file.pdf

To generate a PostScript file, hit the "print" button in xpdf, or run
pdftops:
  pdftops file.pdf

To generate a plain text file, run pdftotext:
  pdftotext file.pdf

There are four additional utilities (which are fully described in
their man pages):

  pdfinfo -- dumps a PDF file's Info dictionary (plus some other
             useful information)
  pdffonts -- lists the fonts used in a PDF file along with various
              information for each font
  pdftoppm -- converts a PDF file to a series of PPM/PGM/PBM-format
              bitmaps
  pdfimages -- extracts the images from a PDF file


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CC="cc"
CXX="CC"
CFLAGS='-g -xs -Xa -xarch=v8plus -mt -xstrconst'
CXXFLAGS='-g -xs -xarch=v8plus -noex -mt'
CPPFLAGS="-I/usr/local/include/freetype2 -I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export CC CXX CPPFLAGS LD LDFLAGS
./configure --prefix=%{prefix} --with-freetype2-library=/usr/local/lib --with-freetype2-includes=/usr/local/include/freetype2 --with-t1-library=/usr/local/lib --with-t1-includes=/usr/local/include --enable-wordlist --enable-multithreaded

cd splash
cp SplashFTFont.cc SplashFTFont.cc.wrong 
#sun's cpp is not as liberal as gcc's
/usr/local/bin/sed -e 's%%#include FT_OUTLINE_H%%#include <freetype/ftglyph.h> \n#include <freetype/ftoutln.h>%%' -e 's%%#include FT_INTERNAL_OBJECTS_H%%#include <freetype/ftsizes.h>%%' SplashFTFont.cc.wrong > SplashFTFont.cc 
cd .. 
make 

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} 



%clean
[ %{buildroot} != "/" ] && [ -d %{buildroot} ] && rm -rf %{buildroot}

%post

%files
%defattr(-, root, root)
%doc ANNOUNCE CHANGES COPYING README INSTALL
%{prefix}/bin
%{prefix}/man
%{prefix}/etc/xpdfrc

%changelog
* Tue Aug 22 2006 John Santel <jmsl@nbcs.rutgers.edu>
- added debian patch 05_freetype-2.2.dpatch from the unstable package 
xpdf_3.01-9 so it builds against freetype-2.2
- added some sed hacks to remove #includes that reference #defines
- added the security patch xpdf-3.01pl2.patch

