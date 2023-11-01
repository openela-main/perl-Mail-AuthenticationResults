Name:           perl-Mail-AuthenticationResults
Version:        2.20210112
Release:        1%{?dist}
Summary:        Object Oriented Authentication-Results Headers
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Mail-AuthenticationResults/
Source0:        http://www.cpan.org/modules/by-module/Mail/Mail-AuthenticationResults-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl >= 0:5.008
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
Object Oriented Authentication-Results email headers.


%prep
%setup -q -n Mail-AuthenticationResults-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%license LICENSE
%doc Changes dist.ini README README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 28 2022 Martin Osvald <mosvald@redhat.com> - 2.20210112-1
- Initial version
