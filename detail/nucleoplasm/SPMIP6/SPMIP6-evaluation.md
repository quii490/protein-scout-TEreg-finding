---
type: protein-evaluation
gene: "SPMIP6"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SPMIP6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SPMIP6 |
| 蛋白名称 | Sperm microtubule inner protein 6 |
| 蛋白大小 | 262 aa / 30.2 kDa |
| UniProt ID | Q8NCR6 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Equatorial segment; Nucleoplasm; Principa (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 262 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=53.7; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | SPMIP6 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.9/100** | 互证: +2 |

### 3. 分析
- HPA: Cytosol; Equatorial segment; Nucleoplasm; Principal piece (Supported)
- PubMed: strict=0, broad=6
- AF pLDDT: 53.7 / PDB: 0
- InterPro: SPMIP6
- Pfam: SMRP1
- PPI degree=0 ChIP: None


### 4. 总体评价
★★★★  **68.9/100**  **nucleoplasm**
Nuclear protein


### 深度机制分析

**精子微管内部蛋白的核质异常定位**：SPMIP6（Sperm microtubule inner protein 6, 262 aa, UniProt Q8NCR6）与SPMIP9同属精子鞭毛轴丝双联微管内部蛋白家族。其功能注释为参与精子尾部的manchette内转运和中段形成，可能在体细胞增殖中也发挥作用（UniProt annotation）。InterPro SPMIP6（IPR028195）和Pfam SMRP1（PF15181）均为精子微管特异性结构域。HPA标注该蛋白在Cytosol、Equatorial segment、Nucleoplasm和Principal piece中为Supported级别定位——其多定位特征提示该蛋白可能存在非鞭毛的体细胞功能。

**低结构置信度与功能解析困难**：AlphaFold pLDDT=53.7与SPMIP9（55.3）类似，属于极低置信度区间。这种低置信度通常由以下因素引起：(1) 蛋白在溶液中为天然无序状态；(2) 缺乏同源模板导致AF2无法准确折叠；(3) 蛋白需要结合伴侣蛋白才能获得稳定构象。对于微管内部蛋白（MIP），其正确折叠往往依赖于微管腔内的限制性环境和相邻tubulin异二聚体的模板效应，游离态的高无序度可以理解。

**无PPI网络的"盲区"**：与SPMIP9同样地，PPI degree=0、PubMed=0使该蛋白处于完全的实验真空。唯一的文献支持为间接相关的6篇论文（PMIDs:28863455, 28601408, 25635517）。SPMIP6的核质定位（Supported而非Approved）来源于HPA抗体HPA041767，其特异性未经额外验证。在缺乏正交证据的情况下（如CRISPR敲除后的亚细胞蛋白质组学分析），核质定位信号应被视为不确定。

**体细胞增殖功能的微弱暗示**：UniProt注释中"May play a potential role in somatic cell proliferation"提供了唯一的功能扩展线索。若SPMIP6确实参与体细胞增殖调控，则可能在细胞周期的某个阶段进入核内执行功能——类似于核内actin和myosin在基因转录和染色质重塑中的作用。然而，SPMIP6的结构域（SMRP1）与chromatin remodeling因子之间不存在任何已知联系。建议在TE筛选中赋予最低优先级，与SPMIP9同属"暗蛋白"类别。


### 补充分析 (UniProt API)

**蛋白全称**: Sperm microtubule inner protein 6

**功能**: May participate in intramanchette transport and midpiece formation of the sperm tail. May play a potential role in somatic cell proliferation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR028195 |
| Pfam | PF15181 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Sperm microtubule inner protein 6

**功能**: May participate in intramanchette transport and midpiece formation of the sperm tail. May play a potential role in somatic cell proliferation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR028195 |
| Pfam | PF15181 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---