---
type: protein-evaluation
gene: "B7Z1G4"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## B7Z1G4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | B7Z1G4 |
| 蛋白名称 | IMP dehydrogenase |
| 蛋白大小 | 357 aa / 39.0 kDa |
| UniProt ID | B7Z1G4 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 357 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=91.1; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Aldolase_TIM; CBS_dom; CBS_dom_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=91.1 PDB=0
- InterPro: Aldolase_TIM; CBS_dom; CBS_dom_sf
- Pfam: CBS; IMPDH
- PPI degree=0 ChIP: None


### 深度机制分析

B7Z1G4编码IMP脱氢酶（IMPDH）的TrEMBL变体，其结构域架构由两个保守区域组成：N端TIM桶状折叠的催化结构域（Aldolase_TIM、IPR013785、Pfam IMPDH）负责将IMP氧化为XMP的速率限制催化步骤；C端CBS结构域对（CBS_dom、CBS_dom_sf、IPR000644、IPR046342、Pfam CBS）形成串联的胱硫醚-beta-合成酶二聚化模块，负责变构调控——响应ATP/AMP比值以调控酶活性。

357 aa（39.0 kDa）的紧凑分子量反映该TrEMBL变体可能缺少全长IMPDH的N端延伸区域。AlphaFold pLDDT高达91.1，在所有75个评估蛋白中结构质量位列前茅，且0个PDB实验结构赋予其高新颖性。CBS域对的存在暗示ATP/AMP比值可能作为该酶活性的直接代谢传感器。

TE调控相关性的机制推论基于两个互不排斥的假说：**核酸结合假说**——IMPDH被报道具有单链核酸结合活性，若该TrEMBL变体保留此功能，其可能直接结合TE衍生的RNA或DNA，影响TE转录本的稳定性或反转录效率（尤其对LINE-1的TPRT机制）；**核苷酸池调控假说**——IMPDH作为GTP从头合成的限速酶，其活性直接决定细胞内dNTP/GTP池大小，而逆转录转座子的反转录步骤对dNTP浓度高度敏感。通过调控GTP水平，IMPDH可能间接但不系统地影响所有正在活跃转座TE的复制效率。

但该变体无核定位GO-CC注释（核定位特异性仅4/10），PubMed=0，PPI degree=0。虽然pLDDT达91.1的结构质量极高，但功能性TE调控的机制链条过长，归一化总分67.8/100，不建议优先靶标地位。若未来获得该变体全长功能注释和核苷酸代谢与TE活性关联的直接数据，其代谢调控TE的假说将具有概念新颖性。

### 4. 总体评价
**67.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: IMP dehydrogenase

**功能**: Catalyzes the conversion of inosine 5'-phosphate (IMP) to xanthosine 5'-phosphate (XMP), the first committed and rate-limiting step in the de novo synthesis of guanine nucleotides, and therefore plays an important role in the regulation of cell growth. Could also have a single-stranded nucleic acid-binding activity and could play a role in RNA and/or DNA metabolism. It may also have a role in the development of malignancy and the growth progression of some tumors

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR013785 |
| InterPro | IPR000644 |
| InterPro | IPR046342 |
| InterPro | IPR005990 |
| InterPro | IPR015875 |
| InterPro | IPR001093 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE 调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-B7Z1G4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B7Z1G4
