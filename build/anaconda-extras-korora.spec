Name:           anaconda-extras-korora
Version:        0.1
Release:        1%{?dist}
Summary:        Korora customisation for the anaconda

Group:          Applications/System
License:        GPLv3
URL:            https://github.com/kororaproject/kp-anaconda-extras-korora.spec
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel
Requires:       anaconda

%description
%{summary}.


%prep
%setup -q


%install
mkdir -p %{buildroot}%{python3_sitelib}/pyanaconda/installclasses/

install -m 0644 korora.py %{buildroot}%{python3_sitelib}/pyanaconda/installclasses/


%clean
rm -rf %{buildroot}


%files
%{python3_sitelib}/pyanaconda/installclasses/korora.py


%changelog
* Mon Jul 31 2017 Ian Firns <firnsy@kororaproject.org> - 0.1-1
- Initial spec.
