
#include <iostream>
#include<json/json.h>
#include<fstream>

class rect_3d_depth
{
    public:
    //cv::Rect obj_rect;
    int x=100;
    int y=101;
    int w=102;
    int h=103;
    float distanse{-1.0};
    long frameid{-1};
    float width{-1.0};
};
std::vector<rect_3d_depth> vecters;
rect_3d_depth rd1;
rect_3d_depth rd2;
int main(int argc ,char ** argv)
{
      Json::Value root;
    Json::Value rects;
    vecters.push_back(rd1);
    vecters.push_back(rd1);
Json::FastWriter fwriter;
Json::StyledWriter swriter;
    for(rect_3d_depth r_3_d :vecters )
    {
        Json::Value rect;
        rect["x"] = r_3_d.x;
        rect["y"] = r_3_d.y;
        rect["width"] = r_3_d.w;
        rect["height"] = r_3_d.h;
        rect["dist"] = r_3_d.distanse;
         rect["realwidth"] = r_3_d.width;
         rects.append(rect);
    }

    root["frameid"]=1;
    root["frametime"]=32;
     root["rects"]=rects;
     std::ofstream os;
     os.open("112.json",std::ios::out | std::ios::app);
     if(!os.is_open())
     {
        std::cout<<"failed "<<std::endl;
     }
     std::string jsstr = swriter.write(root);
    os<<jsstr<<std::endl;
    os.close();
    // os.write(jsstr);

}