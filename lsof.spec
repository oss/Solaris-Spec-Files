Summary: Open file lister
Name: lsof
Version: 4.63
Release: 1
Group: System Environment/Base
License: BSD type
Source: lsof_%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%define lsof_dir lsof_%{version}

%description
Lsof lists information about files opened by processes.
An open file may be a regular file, a directory, a block special file,
a character special file, an executing text reference, a library, a
stream or a network file (Internet socket, NFS file or UNIX domain
socket.) A specific file or all the files in a file system may be
selected by path.

%prep
%setup -n lsof -c -T
%setup -n lsof -D -T -a 0 -q
cd %{lsof_dir}
tar xf %{lsof_dir}_src.tar

%build
cd %{lsof_dir}
cd %{lsof_dir}_src
/bin/echo "y\nn\n" | ./Configure solariscc
make
make install

%install
cd %{lsof_dir}
cd %{lsof_dir}_src
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8
install lsof $RPM_BUILD_ROOT/usr/local/bin/lsof
install -m 0444 lsof.8 $RPM_BUILD_ROOT/usr/local/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc 00*
%attr(2755,root,sys) /usr/local/bin/lsof
/usr/local/man/man8/lsof.8
