Summary: PEAR: Benchmark PHP scripts
Name: pear-Benchmark
Version: 1.2.7
Release: 2 
License: PHP/BSD
Group: Development/Libraries
Source: Benchmark-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: php

%description
Framework to benchmark PHP scripts or function calls.

%prep
%setup -q -n Benchmark-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/Benchmark

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cd Benchmark
cp Iterate.php %{buildroot}/usr/local/lib/php/Benchmark
cp Profiler.php %{buildroot}/usr/local/lib/php/Benchmark
cp Timer.php %{buildroot}/usr/local/lib/php/Benchmark

%files
%defattr(-,root,bin)
   /usr/local/lib/php/Benchmark/Iterate.php
   /usr/local/lib/php/Benchmark/Profiler.php
   /usr/local/lib/php/Benchmark/Timer.php
%doc

%changelog
* Mon Jul 27 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.7-1
- Fixed php requires.

