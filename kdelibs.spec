Name:		kdelibs
Summary:	K Desktop Environment - Libraries
Version:	3.0.1
Release:	1ru
Group:		Graphical desktop/KDE
License:	ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
URL:		http://www.kde.org/
Packager:	Mandrake Linux KDE Team <kde@mandrakesoft.com>
BuildRoot:	%_tmppath/%name-%version-%release-root
PreReq:		arts >= 1.0.0
Source:		kdelibs-%{version}.tar.bz2
Obsoletes:	kdelibs3.0 kdelibs3


%description
Libraries for the K Desktop Environment.


%package devel
Group:		Development/KDE and QT
Summary:	Header files and documentation for compiling KDE applications.
PreReq:		%name = %version-%release, qt3-devel

%description devel
This package includes the header files you will need to compile applications 
for KDE. Also included is the KDE API documentation in HTML format for easy 
browsing.




%prep

%setup -q -n kdelibs-%{version}

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
QTDIR="/usr/local/qt" \
LD_LIBRARY_PATH="$QTDIR/lib:/usr/local/lib:$LD_LIBRARY_PATH" \
LD_RUN_PATH="/usr/local/qt/lib:/usr/local/lib" \
./configure --prefix=/usr/local --disable-pcre


make

%install
rm -fr %buildroot

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot


%files
%defattr(-,root,root,-)

/usr/local/bin
/usr/local/lib
/usr/local/share


%files devel
%defattr(-,root,root,-)
/usr/local/include/*
