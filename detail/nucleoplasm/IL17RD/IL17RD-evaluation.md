---
type: protein-evaluation
gene: "IL17RD"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## IL17RD 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | IL17RD |
| 蛋白名称 | Interleukin-17 receptor D |
| 蛋白大小 | 739 aa / 82.4 kDa |
| UniProt ID | Q8NFM7 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Golgi apparatus; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 739 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=58 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=68.3; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | IL-17_rcpt-like; IL17R_D_N; SEFIR_dom |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=26 |
| **加权总分** | | | **114/180** | |
| **归一化总分** | | | **63.4/100** | 互证: +2 |

### 3. 分析
- Golgi apparatus; Nucleoplasm (Supported)
- PubMed strict=58 broad=124
- AF pLDDT=68.3 PDB=0
- InterPro: IL-17_rcpt-like; IL17R_D_N; SEFIR_dom
- Pfam: IL17R_D_N; SEFIR
- PPI degree=26 ChIP: None
23643382: Mutations in FGF17, IL17RD, DUSP6, SPRY4, and FLRT3 are identified in individual | 20301509: Isolated Gonadotropin-Releasing Hormone (GnRH) Deficiency. | 33436016: Interleukin-17 receptor D (Sef) is a multi-functional regulator of cell signalin

### 4. 总体评价
**63.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Interleukin-17 receptor D

**功能**: Feedback inhibitor of fibroblast growth factor mediated Ras-MAPK signaling and ERK activation (PubMed:12807873, PubMed:12958313). Regulates the nuclear ERK signaling pathway by spatially blocking nuclear translocation of activated ERK without inhibiting cytoplasmic phosphorylation of ERK (PubMed:15239952). Mediates JNK activation and may be involved in apoptosis (By similarity). May inhibit FGF-induced FGFR1 tyrosine phosphorylation (By similarity). Might have a role in the early stages of fate 

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR039465 |
| InterPro | IPR031951 |
| InterPro | IPR013568 |
| InterPro | IPR035897 |
| Pfam | PF16742 |
| Pfam | PF08357 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

IL17RD（Interleukin-17 receptor D，也称Sef）是一个具有明确核信号调控功能的跨膜受体蛋白。其结构域架构包含三个关键模块：N端IL17R_D_N域（PF16742，IPR039465）、IL-17受体样胞外域（IPR035897）和C端SEFIR结构域（PF08357，IPR013568）。SEFIR结构域是IL-17受体家族的特征性信号结构域，与TIR结构域具有结构同源性，介导下游信号转导。AlphaFold v6预测整体pLDDT=68.3，其中739个氨基酸中广泛存在折叠良好的结构域和无序区域交替的特征，这与跨膜受体的典型结构特征一致——胞外域和跨膜区折叠相对有序，而胞内域（尤其SEFIR域周围）可能包含更多柔性区域用于信号复合体组装。

IL17RD的核心机制已被阐明：作为FGF介导的Ras-MAPK信号通路的反馈抑制因子（PMID:12807873、PMID:12958313），其关键功能是空间上阻断活化ERK的核转位，同时不影响ERK在胞质中的磷酸化（PMID:15239952）。这一机制使IL17RD成为核信号门控的关键调控节点——它通过物理阻截而非生化抑制来调控MAPK信号的核内输出。此外，IL17RD还介导JNK活化并可能参与凋亡调控（By similarity），以及抑制FGF诱导的FGFR1酪氨酸磷酸化，构成了一个多层面的RTK信号负反馈调控网络。

PPI网络较为丰富，STRING记录26个互作伙伴，包括FGFR1（combined score=750）、FLG（750）和PTP4A1（768），BioGRID还鉴定到BTRC（β-TrCP E3泛素连接酶）、FBXW11和NR3C1（糖皮质激素受体）。这些互作提示IL17RD可能通过泛素化途径调控蛋白质稳定性，并通过与核受体（NR3C1）的潜在关联参与转录调控。值得注意的是，HPA IF定位于高尔基体和核质（Supported），其核质定位与ERK核转位阻截功能高度一致。

尽管PubMed strict=58篇（broad=124篇），已有相当研究基础，IL17RD在TE调控中的角色尚未被探索。其作为核信号门控的独特功能模式——空间阻断而非生化抑制——提供了一个引人注目的假说：IL17RD可能通过类似的机制调控TE相关转录因子的核转位或TE衍生序列激活的信号通路。研究热度的提升（主要集中于GnRH缺乏症相关突变，PMID:23643382）提示该领域正在快速发展。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PTP4A1 | STRING | 768 |
| FGFR1 | STRING | 750 |
| FLG | STRING | 750 |
| BTRC | BioGRID | 1 |
| FBXW11 | BioGRID | 1 |
| PTPRD | BioGRID | 1 |
| LTB4R2 | BioGRID | 1 |
| NR3C1 | BioGRID | 1 |



### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/IL17RD

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000144730-IL17RD

![](https://images.proteinatlas.org/43550/2212_H3_25_blue_red_green.jpg)
![](https://images.proteinatlas.org/43550/2212_H3_28_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000144730-IL17RD

![](https://images.proteinatlas.org/43550/2212_H3_25_blue_red_green.jpg)
![](https://images.proteinatlas.org/43550/2212_H3_28_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000144730-IL17RD

![](https://images.proteinatlas.org/43550/2212_H3_25_blue_red_green.jpg)
![](https://images.proteinatlas.org/43550/2212_H3_28_blue_red_green.jpg)