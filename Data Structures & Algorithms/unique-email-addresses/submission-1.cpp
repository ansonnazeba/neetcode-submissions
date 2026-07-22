#include <unordered_set>
#include <string>

using namespace std;

class Solution {
public:
// extract local and domain names
    int numUniqueEmails(vector<string>& emails) {
        std::unordered_set<string> mails;

        for (auto email: emails){
            auto atPos = email.find('@');
            auto localName = email.substr(0, atPos);
            auto domainName = email.substr(atPos + 1);

            // filtering the localName
            localName.erase(remove(localName.begin(), localName.end(), '.'), localName.end());

            auto plusPos = localName.find('+');
            localName = plusPos != string::npos? localName.substr(0, plusPos): localName;

            mails.insert(localName + domainName);
        }

        return mails.size();
    }
};