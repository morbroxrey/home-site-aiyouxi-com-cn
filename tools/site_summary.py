class SiteInfo:
    def __init__(self, name, url, tags, description):
        self.name = name
        self.url = url
        self.tags = tags
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "tags": self.tags,
            "description": self.description
        }


class SiteSummaryBuilder:
    def __init__(self, sites=None):
        self.sites = sites if sites else []

    def add_site(self, site):
        self.sites.append(site)

    def build_summary(self):
        lines = []
        lines.append("=" * 50)
        lines.append("站点资料结构化摘要")
        lines.append("=" * 50)
        for site in self.sites:
            lines.append(f"名称：{site.name}")
            lines.append(f"URL：{site.url}")
            lines.append(f"标签：{', '.join(site.tags)}")
            lines.append(f"说明：{site.description}")
            lines.append("-" * 40)
        return "\n".join(lines)

    def print_summary(self):
        print(self.build_summary())


def load_default_sites():
    return [
        SiteInfo(
            name="爱游戏门户",
            url="https://home-site-aiyouxi.com.cn",
            tags=["爱游戏", "游戏资讯", "玩家社区"],
            description="专注于提供最新游戏动态、攻略评测和玩家交流的综合游戏站点。"
        ),
        SiteInfo(
            name="爱游戏攻略站",
            url="https://home-site-aiyouxi.com.cn/strategy",
            tags=["爱游戏", "攻略", "技巧"],
            description="汇集大量游戏攻略和实用技巧，帮助玩家快速提升游戏体验。"
        ),
        SiteInfo(
            name="爱游戏论坛",
            url="https://home-site-aiyouxi.com.cn/forum",
            tags=["爱游戏", "论坛", "互动"],
            description="开放的游戏社区，玩家可自由发帖、讨论、分享游戏心得。"
        )
    ]


def generate_summary_for_keyword(sites, keyword):
    matched = [s for s in sites if keyword.lower() in s.name.lower() or keyword.lower() in [t.lower() for t in s.tags]]
    if not matched:
        return f"未找到与关键词“{keyword}”相关的站点。"
    builder = SiteSummaryBuilder(matched)
    return builder.build_summary()


def main():
    default_sites = load_default_sites()
    builder = SiteSummaryBuilder(default_sites)
    print("【默认站点摘要】")
    builder.print_summary()
    print("\n")
    keyword = "爱游戏"
    print(f"【按关键词“{keyword}”筛选摘要】")
    result = generate_summary_for_keyword(default_sites, keyword)
    print(result)


if __name__ == "__main__":
    main()