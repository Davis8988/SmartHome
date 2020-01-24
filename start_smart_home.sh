RED='\033[1;31m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
ORANGE='\033[0;33m'
GRAY='\033[0;37m'
NC='\033[0m' # No Color

echo -e " \n${RED}"
echo -e "        .    ${GRAY}~~~~~${RED}"
echo -e "      ./ \\. ||"
echo -e "    ./ ./  \\||"
echo -e "  ./ ./  ./ ||"
echo -e " /  /   /  /  \\"
echo -e "${BLUE}================"
echo -e "${BLUE}==            =="
echo -e "== ${CYAN}Smart Home${BLUE} =="
echo -e "${ORANGE}==            =="
echo -e "================\n${NC}"


echo Changing permissions
sudo chmod -R 777 ./node-red

echo Starting SmartHome stack..
docker-compose up -d
