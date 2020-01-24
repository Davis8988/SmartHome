RED='\033[0;31m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
ORANGE='\033[0;33m'
NC='\033[0m' # No Color

echo -e "\n${RED}      /\\"
echo -e "    /  / \\"
echo -e "  /  /   / \\"
echo -e "/   /  /  / \\"
echo -e "${BLUE}=============="
echo -e "${BLUE}=            ="
echo -e "= ${CYAN}Smart Home${BLUE} ="
echo -e "${ORANGE}=            ="
echo -e "==============\n${NC}"


echo Changing permissions
sudo chmod -R 777 ./node-red

echo Starting SmartHome stack..
docker-compose up -d
