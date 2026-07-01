---
type: protein-evaluation
gene: "CFAP68"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CFAP68 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CFAP68 |
| 蛋白名称 | Cilia- and flagella-associated protein 68 |
| 蛋白大小 | 150 aa / 17.8 kDa |
| UniProt ID | Q9H5F2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Enhanced) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 150 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=1 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=69.0; PDB=2 |
| 调控结构域 | 4/10 | ×2 | 8.0 | CFAP68; CFAP68/107 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
- HPA: Nucleoplasm (Enhanced)
- PubMed: strict=1, broad=1
- AF pLDDT: 69.0 / PDB: 2
- InterPro: CFAP68; CFAP68/107
- Pfam: CFAP68
- PPI degree=0 ChIP: None
38835510: Gene-deficient mouse model established by CRISPR/Cas9 system reveals 15 reproduc

### 4. 总体评价
★★★★  **72.1/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Cilia- and flagella-associated protein 68

**功能**: Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR009524 |
| InterPro | IPR037662 |
| Pfam | PF06608 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Cilia- and flagella-associated protein 68

**功能**: Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR009524 |
| InterPro | IPR037662 |
| Pfam | PF06608 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H5F2-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 1**

| 38835510 | Gene-deficient mouse model established by CRISPR/Cas9 system reveals 15 reproductive organ-enriched genes dispensable fo | Front Cell Dev Biol 2024 |

### 深度机制分析

CFAP68（150 aa, 17.8 kDa）是一个高度特化的纤毛相关蛋白，其结构域极为精简——仅含单个CFAP68结构域（IPR009524, PF06608），几乎占据整个蛋白序列。该蛋白属于纤毛轴丝双联微管（DMT）内部蛋白（MIP）家族，定位于动力蛋白修饰的DMT内部，对运动纤毛的正常跳动必不可少。因蛋白极小（仅150 aa），AlphaFold预测pLDDT仅69.0，且无长程有序结构，但已有2个PDB条目提供实验结构验证。

功能上，CFAP68作为纤毛内部微管结合蛋白（MIP），在纤毛轴丝这一精密分子机器中扮演结构稳定和机械传导角色。其精确的MIP定位由鞭毛内运输（IFT）系统介导，在纤毛组装过程中被递送至生长的轴丝远端。CRISPR/Cas9基因敲除小鼠模型揭示了CFAP68在雄性生殖器官中的表达及其对生育能力的贡献（PMID:38835510），其中15个生殖器官富集基因被鉴定为可丧失，提示CFAP68在精子鞭毛运动中发挥作用。

HPA将CFAP68定位于Nucleoplasm（Enhanced级别）是一个意外发现。该蛋白已知的纤毛功能全部在胞质纤毛轴丝中，核定位证据可能是以下机制之一：（1）CFAP68在核纤层或核内肌动蛋白丝上有次要结合位点；（2）IF抗体的交叉反应；（3）CFAP68确实具有尚未发现的核内功能。PPI网络完全空白（degree=0），这在功能明确的小蛋白中并不罕见——MIP可能直接结合微管蛋白异二聚体而非通过经典PPI伙伴发挥功能。

从TE调控角度，若CFAP68的核定位是真实的，其作为微管结合蛋白可能在核内有丝分裂纺锤体组装或染色质分离中具有次要功能。纤毛蛋白的核定位也有先例，部分纤毛蛋白同时参与DNA损伤应答或细胞周期调控。但现有证据薄弱——蛋白太小（150 aa）、无已知DNA/RNA结合域、无可识别的核定位信号（NLS），TE调控潜力需要更严谨的IF验证和核定位机制解析才能确认。建议使用CFAP68特异性敲除细胞系进行亚细胞组分分离和质谱验证，排除IF假阳性后再探讨核内功能。

