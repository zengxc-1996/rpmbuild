Name:sqlite-autoconf		
Version: 3340000	
Release: 1%{?dist}
Summary:slqite3 is a db	

#Group:		
License:GPL	
URL:www.test.com		
Source0:sqlite-autoconf-3340000.tar.gz	

BuildRequires: make gcc	
#Requires:	

%description
A simple RPM package to print Hello World

%prep
%setup -q

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT/*
make install DESTDIR=%{?buildroot}

%files
%defattr(-,root,root)
/usr/local