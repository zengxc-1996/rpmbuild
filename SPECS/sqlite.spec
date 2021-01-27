Name: sqlite3		
Version: 3.34
Release: 1%{?dist}
Summary: sqlite3 database

#Group:		
License:GPL	
#URL:www.test.com		
Source0: %{name}-%{version}.tar.gz	

BuildRequires: make gcc	
#Requires:	

%description
sqlite3.34

%prep
%setup -q

%build
./configure --prefix=%{_usr}
make

%install
rm -rf $RPM_BUILD_ROOT/*
make install DESTDIR=%{?buildroot}

%files
%defattr(-,root,root)
/usr

%doc README.txt

%changelog