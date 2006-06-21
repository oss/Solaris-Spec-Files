Summary: 	PEAR: Element for HTML_QuickForm to enable a suggest search.
Name: 		pear-HTML_QuickForm_Livesearch
Version: 	0.2.0
Release: 	1
License: 	PHP License
Group: 		Development/Libraries
Source: 	HTML_QuickForm_Livesearch-%{version}.tgz
URL: 		http://pear.php.net/package/HTML_QuickForm_Livesearch
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Prefix: 	%{_prefix}
Requires: 	pear-HTML_Common, pear-HTML_QuickForm, pear-HTML_AJAX

%description
This package adds an element to the PEAR::HTML_QuickForm package to 
dynamically create an HTML input text element that at every keypressed 
javascript event, returns a list of options in a dynamic dropdown select 
box(live dropdown select).
This element use AJAX (Communication from JavaScript to your browser 
without reloading the page).
This type of livesearch is useful when you have a form with a dropdown 
list with a large number of row.

%prep
%setup -q -n HTML_QuickForm_Livesearch-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/HTML/QuickForm
mkdir -p %{buildroot}/usr/local/lib/php/doc/HTML_QuickForm_Livesearch

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp livesearch_select.php %{buildroot}/usr/local/lib/php/HTML/QuickForm/
cp live.js %{buildroot}/usr/local/lib/php/HTML/QuickForm/
cp -r example/ %{buildroot}/usr/local/lib/php/HTML/QuickForm/

%files
%defattr(-,root,bin)
%dir /usr/local/lib/php/HTML/QuickForm
/usr/local/lib/php/HTML/QuickForm/*

