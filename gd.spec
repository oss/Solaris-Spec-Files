%define name gd
%define version 1.8.4
%define release 2
%define prefix /usr/local

Summary: A graphics library for fast image creation
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Graphics/Libraries
Source0: http://www.boutell.com/gd/http/gd-1.8.4.tar.gz
Buildroot: /var/local/tmp/%{name}-root
requires: libpng >= 1.0.12, zlib >= 1.1.3, libjpeg >= 6b

%description
gd is a graphics library. It allows your code to quickly draw images complete with lines, arcs, text, multiple colors, cut and paste from other images, and flood fills, and write out the result. As a PNG or JPEG file. This is particularly useful in World Wide Web applications, where PNG and JPEG are two of the formats accepted for inline images by most browsers

%prep
%setup

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{prefix}/lib
mkdir $RPM_BUILD_ROOT/%{prefix}/bin
mkdir $RPM_BUILD_ROOT/%{prefix}/include
make INSTALL_LIB=$RPM_BUILD_ROOT%{prefix}/lib INSTALL_INCLUDE=$RPM_BUILD_ROOT%{prefix}/include INSTALL_BIN=$RPM_BUILD_ROOT%{prefix}/bin  install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{prefix}/bin/*
%{prefix}/lib/*
%{prefix}/include/*
