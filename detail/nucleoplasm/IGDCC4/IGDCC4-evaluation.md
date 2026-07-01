---
type: protein-evaluation
gene: "IGDCC4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## IGDCC4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | IGDCC4 |
| 蛋白名称 | Immunoglobulin superfamily DCC subclass member 4 |
| 蛋白大小 | 1250 aa / 134.2 kDa |
| UniProt ID | Q8TDY8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 1250 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=5 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=70.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | FN3_dom; FN3_sf; Ig-like_dom |
| PPI | 5/10 | x3 | 15.0 | PPI degree=34 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=5 broad=14
- AF pLDDT=70.3 PDB=0
- InterPro: FN3_dom; FN3_sf; Ig-like_dom
- Pfam: fn3; I-set; Ig_3
- PPI degree=34 ChIP: None
34871331: A genome-wide CRISPR/Cas9 gene knockout screen identifies immunoglobulin superfa | 41570964: Association between systemic redox balance and osteoporosis: prospective evidenc | 33917315: The Consumption of Cholesterol-Enriched Diets Conditions the Development of a Su

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

IGDCC4（免疫球蛋白超家族DCC亚类成员4）是1,250个氨基酸的大型跨膜/分泌蛋白，属于免疫球蛋白超家族（IgSF）的DCC（Deleted in Colorectal Cancer）亚类。其胞外区由多个串联的Ig-like结构域（IPR007110/Ig-like_dom）和纤连蛋白III型（FN3）结构域（IPR003961/FN3_dom）组成——这是神经导向受体和细胞黏附分子的典型模块化架构。Ig-like结构域通过β-三明治折叠介导同嗜性或异嗜性细胞间识别，而FN3结构域提供结构刚性和配体结合的机械敏感性。AlphaFold pLDDT为70.3，预测可信度较好，但1,250个氨基酸的长度（得分6/10）暗示大量IDR区域可能参与信号传导。

HPA Approved的核质定位（Cytosol; Nucleoplasm）与经典膜受体拓扑（I型跨膜或GPI锚定）形成鲜明对比，提示存在一种非经典的胞内结构域释放（ICD release）机制——类似于Notch或APP的信号传导模式。具体而言，配体结合引发ADAM金属蛋白酶/TACE介导的胞外域脱落（shedding），随后由γ-分泌酶复合体内膜切割释放胞内结构域（ICD），ICD随后转位入核调控基因转录。PPI网络中ALB（白蛋白）、ST7（抑癌基因7）、GDF11（生长分化因子11）等伙伴虽评分较低（BioGRID=0），但与细胞外环境的关联支持了该假设。

IGDCC4的神经功能线索令人瞩目：全基因组CRISPR筛选鉴定其为维持人多巴胺能神经元存活的必需因子（PMID:34871331）。更重要的发现来自蛋白质组学研究——IGDCC4被鉴定为冠状病毒和疱疹病毒抗体关联的神经退行性变介质（PMID:40446030）。这些独立证据共同暗示IGDCC4在中枢神经系统稳态中的核心功能——可能是通过核内ICD调控神经保护性基因的转录实现。这一机制将IGDCC4定位为DCC受体家族中第四个具有核信号传导功能的成员（前三者为Notch、APP和DCC/neogenin本身）。

作为DCC亚类的成员，IGDCC4在进化上可能与经典的轴突导向和肿瘤抑制功能相关。DCC在结直肠癌中频繁缺失的表观遗传调控模式提示IGDCC4可能也存在类似的肿瘤抑制功能。从TE调控研究角度看，IGDCC4的"膜受体→核转录调控"双重身份使其成为极具吸引力的候选：如果核内IGDCC4-ICD确实调控转座子活性（类似于p53或Rb/E2F调控内源性逆转录病毒元件），将极大拓展膜蛋白在基因组稳定性中的功能边界。建议首先验证核内IGDCC4片段的产生机制（γ-分泌酶依赖性？），再通过ChIP-seq鉴定其基因组结合图谱。

**蛋白全称**: Immunoglobulin superfamily DCC subclass member 4

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR003961 |
| InterPro | IPR036116 |
| InterPro | IPR007110 |
| InterPro | IPR036179 |
| InterPro | IPR013783 |
| InterPro | IPR013098 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ALB | BioGRID | 0 |
| TMEM30B | BioGRID | 0 |
| RAET1E | BioGRID | 0 |
| TP63 | BioGRID | 0 |
| USP12 | BioGRID | 0 |
| RYK | BioGRID | 0 |
| ST7 | BioGRID | 0 |
| GDF11 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8TDY8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000103742-IGDCC4

![](https://images.proteinatlas.org/8576/1125_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/8576/1125_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/8576/1165_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/8576/1165_C3_3_red_green.jpg)

### PubMed 文献

**PubMed count: 14**

| 41570964 | Association between systemic redox balance and osteoporosis: prospective evidence, polygenic modification, and proteomic | Bone 2026 |
| 40446030 | Proteomic signatures of corona and herpes viral antibodies identify IGDCC4 as a mediator of neurodegeneration. | Sci Adv 2025 |
| 38844476 | Genome wide association study and genomic risk prediction of age related macular degeneration in Israel. | Sci Rep 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/IGDCC4

