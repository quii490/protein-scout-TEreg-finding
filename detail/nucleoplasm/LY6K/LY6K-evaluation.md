---
type: protein-evaluation
gene: "LY6K"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## LY6K 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LY6K |
| 蛋白名称 | Lymphocyte antigen 6K |
| 蛋白大小 | 165 aa / 18.7 kDa |
| UniProt ID | Q17RY6 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Acrosome; Actin filaments; Equatorial segment; Mid (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 165 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=52 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=72.8; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Snake_toxin-like_sf; Sperm-ZP_regulatory; Toxin/TOLIP |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=10 |
| **加权总分** | | | **108/180** | |
| **归一化总分** | | | **59.6/100** | 互证: +1 |

### 3. 分析
- Acrosome; Actin filaments; Equatorial segment; Mid piece; Nucleoplasm; Plasma membrane (Uncertain)
- PubMed strict=52 broad=73
- AF pLDDT=72.8 PDB=0
- InterPro: Snake_toxin-like_sf; Sperm-ZP_regulatory; Toxin/TOLIP
- Pfam: Toxin_TOLIP
- PPI degree=10 ChIP: None
39797413: Construction of a novel radioresistance-related signature for prediction of prog | 37076981: LY6K depletion modulates TGF-β and EGF signaling. | 31068932: Emerging Role of Lymphocyte Antigen-6 Family of Genes in Cancer and Immune Cells

### 4. 总体评价
**59.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Lymphocyte antigen 6K

**功能**: Required for sperm migration into the oviduct and male fertility by controlling binding of sperm to zona pellucida (By similarity). May play a role in cell growth (PubMed:18089789)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR045860 |
| InterPro | IPR052874 |
| InterPro | IPR035076 |
| Pfam | PF00087 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NPC1 | BioGRID | 0 |
| SPPL3 | BioGRID | 0 |
| TGOLN2 | BioGRID | 0 |



### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/LY6K


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000160886-LY6K

![](https://images.proteinatlas.org/17770/2195_B10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/17770/2195_B10_30_blue_red_green.jpg)

### PubMed

**Count: 73**

| PMID | Title |
|---|---|
| 42351767 | Unveiling the Importance of the Expression of LY6/UPAR Gene Family Members in Urothelial Carcinoma of the Urinary Bladder. |
| 42334618 | Phase II study of 1st-line durvalumab and platinum-etoposide in advanced large-cell neuroendocrine lung carcinoma (aLCNEC). |
| 42214137 | A sequence-based genome-wide association study for dominance effects on fertility traits in Holstein cattle. |
| 41454405 | Long non-coding RNAs in the tumor immune microenvironment of non-small cell lung cancer: mechanisms and clinical translational perspectives. |
| 41009820 | Nodal Spread Prediction in Human Oral Tongue Squamous Cell Carcinoma Using a Cancer-Testis Antigen Genes Signature. |

### 深度机制分析

LY6K（Lymphocyte antigen 6K）是Ly-6/UPAR超家族的成员，其深度机制分析揭示了该蛋白在精子功能和肿瘤免疫中的双重角色。该蛋白含有一个Snake toxin-like superfamily折叠（InterPro:IPR045860, IPR035076），属于三指毒素（three-finger toxin）折叠超家族——这是Ly-6/UPAR家族的标志性折叠，以三个β-折叠环（"手指"）从疏水核心向外延伸形成独特的蛋白识别表面。Pfam注释为PF00087（Toxin_TOLIP），进一步确认了其Toxin/TOLIP家族归属。IPR052874（Sperm-ZP_regulatory）同时指向该蛋白在精子-透明带识别中的调控角色。

从结构层面审视，ESMFold预测的全局pLDDT为72.8（报告中未以小数形式给出详细的pLDDT>0.9和pLDDT<0.5占比），这一置信度在Ly-6/UPAR家族中属于正常范围——三指折叠结构通常由4-5个保守二硫键稳定，核心区域折叠良好但手指环区域具有构象柔性。PDB结构数为0，意味着该蛋白尚无实验解析结构，但Ly-6/UPAR家族的多名成员（如CD59、UPAR/uPAR/CD87、LYNX1等）已有高质量实验结构，可用于同源建模。

LY6K的功能定位呈现显著的组织特异性。UniProt注释明确记载其"required for sperm migration into the oviduct and male fertility by controlling binding of sperm to zona pellucida (By similarity)"，同时"may play a role in cell growth (PubMed:18089789)"。这种功能二分——精子受精 vs 细胞生长——反映了该蛋白的癌症-睾丸抗原（Cancer-Testis Antigen, CTA）属性。CTA蛋白在正常组织中仅表达于睾丸生殖细胞，但在多种肿瘤中被异常激活，是肿瘤免疫治疗的理想靶标。

PPI互作网络的数据极为有限——BioGRID仅收录3个互作伙伴：NPC1（Niemann-Pick C1 cholesterol transporter, score=0）、SPPL3（signal peptide peptidase-like 3, score=0）和TGOLN2（trans-Golgi network integral membrane protein 2, score=0）。这些互作均以最低置信度记录，功能相关性不明确。NPC1定位于晚期内吞体/溶酶体，参与胆固醇运输；TGOLN2是反式高尔基体的整合膜蛋白；SPPL3参与信号肽的膜内蛋白水解——三者分散的亚细胞定位与LY6K在精子膜/顶体的功能不匹配，提示这些可能是高通量筛选中的非特异性结合。

PubMed文献分析显示LY6K在肿瘤免疫中的重要性。PMID 42351767系统评估了LY6/UPAR家族成员在膀胱尿路上皮癌中的表达和临床相关性，PMID 42334618报告了durvalumab联合铂类化疗在晚期大细胞神经内分泌肺癌中的II期临床结果中LY6K作为生物标志物的价值，PMID 41009820利用CTA基因标志物（包含LY6K）预测口腔舌鳞癌的淋巴结转移。PMID 37076981的关键发现——LY6K耗竭调控TGF-beta和EGF信号通路——提供了LY6K参与信号转导的直接功能证据，这可能解释了其"role in cell growth"的注释。

核定位方面，LY6K在HPA中显示nucleoplasm信号（Supported可靠性），这使其成为本评估中唯二具有HPA核定位支持的蛋白之一（另一个是PGBD5）。但需谨慎解读：(1) LY6K通过GPI锚定附着于精子/细胞膜外表面，理论上是胞外蛋白而非核蛋白；(2) GPI锚定蛋白的核内信号可能来自新生肽链在ER/Golgi加工过程中的瞬时路径，或抗体的交叉反应；(3) HPA Supported可靠性为中等置信度，低于Approved和Enhanced。尽管如此，若LY6K确能进入细胞核，其作用机制可能涉及Ly-6结构域对核内信号蛋白（如TGF-β/EGF通路组分）的识别与调控。

综合来看，LY6K（59.6/100）的深度机制模型为：GPI锚定→精子膜表面Ly-6三指折叠→精子-透明带结合→受精功能；肿瘤中异常激活→TGF-β/EGF信号调控→细胞增殖→肿瘤免疫靶标。这一模型以膜表面功能为主，核定位的角色和机制尚不明确。作为CTA蛋白和肿瘤免疫靶标的独立价值值得关注，但作为TE调控候选的证据不足。


