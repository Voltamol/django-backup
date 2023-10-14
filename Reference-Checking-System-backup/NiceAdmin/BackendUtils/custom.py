import os
import bs4
import json
class TemplateModifier:
    def update_url(self,tag, app_name, attribute="href"):
        assert isinstance(tag, bs4.element.Tag), "expecting type {} not type {}".format(type(bs4.element.Tag), type(tag))
        path = tag.get(attribute)
        if not "html" in path:
            contents = "% static '{}/{}' %".format(app_name, path)
        else:
            path=path.split(".")[0]
            path="_".join(path.split("-"))
            contents="% url '{}:{}' %".format(app_name, path)
        fullpath = "{%s}" % (contents)
        tag.attrs[attribute] = fullpath
        return tag

    def sieve(self,arr,attribute):
        return [
            tag for tag in arr
            if arr
            if  isinstance(tag,bs4.element.Tag)
            if tag.get(attribute)
            if "#" not in tag.get(attribute)
            if "http" not in tag.get(attribute)
            ]

    def IO(self,fullpath,default_tags,app_name):
        with open(fullpath, "r") as html:
            soup = bs4.BeautifulSoup(html,"lxml")
        targets = [self.sieve(soup.find_all(key), default_tags[key]) for key in default_tags]

        for target, attribute in zip(targets, default_tags.values()):
            for tag in target:
                update=self.update_url(tag, app_name, attribute=attribute)
                tag.replaceWith(update)
        
        with open(fullpath, "w") as html:
            print(str(soup.prettify()),file=html)

    def process_file(self,filename,app_name,root,other_tags={}):
        default_tags = dict(a="href",link="href", script="src",img="src", video="src", audio="src")
        assert isinstance(other_tags, dict), "expected type of {}".format(type(dict))
        default_tags.update(other_tags)
        fullpath=os.path.join(root,filename)
        override=self.get_overrides(filename)
        app_name=override if override else app_name
        self.IO(fullpath,default_tags,app_name)

    def get_processed(self):
        try:
            with open("processed.text","r") as records:
                 templates=records.read().split(",")
        except FileNotFoundError:
            return []
        return templates

    def modify_templates(self,app_name):
        current=os.getcwd()
        path=os.path.join(current,app_name,"templates",app_name)
        if not os.path.exists(path):
            raise OSError(f"path {path} does not exist")
        html_files=[
            file for file in os.listdir(path)
            if "html" in file
            if file not in self.get_processed()
            ]
        for file in html_files:
            self.process_file(file,app_name,path)

        print("processed {}".format(html_files))
        return html_files

    def add_django_tag(self,parent,tag_name):
        """adds a django tag like {% load static %} into a specified parent eg <head>...</head>"""
        pass

    def get_overrides(self,filename):
        """gets names of all files which belong to a different app,stored in an external json file"""
        overrides = "overrides.json"
        if os.path.exists(overrides):
            with open(overrides,"r") as file:
                overrides=json.load(file)

            for key in overrides:
                if filename in overrides[key]:
                    return key

        return None
        
    def record_processed_files(self,app_name):
        processed=self.modify_templates(app_name)
        processed=",".join(processed)+","
        with open("processed.text","a") as records:
            records.write(processed)

if __name__=='__main__':
    organizer=TemplateModifier()
    organizer.record_processed_files("enrollment")
    

    
    
