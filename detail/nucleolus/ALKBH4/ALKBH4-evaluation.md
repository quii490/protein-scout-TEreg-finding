---
type: protein-evaluation
gene: "ALKBH4"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ALKBH4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ALKBH4 / ABH4 |
| 蛋白大小 | 302 aa / ~33.8 kDa |
| UniProt ID | Q9NXW9 |
| 评估日期 | 2026-05-29 |

**IF 图像**: 暂无IF数据

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 6 | ×4 | 24 | UniProt: Nucleus + Nucleolus; 但 Cytoplasm + Midbody 共存 |
| 📏 蛋白大小 | 10 | ×1 | 10 | 302 aa，200–800 最优区间 |
| 🆕 研究新颖性 | 10 | ×5 | 50 | PubMed 14 篇（≤20） |
| 🏗️ 三维结构 | 8 | ×3 | 24 | AlphaFold pLDDT 均值 89.4，87% >70；无 PDB |
| 🧬 调控结构域 | 7 | ×2 | 14 | 新颖基线；Fe2OG dioxygenase 域，非染色质特异性 |
| 🔗 PPI | 4/10 | ×3 | **12** | 详见 3.6 PPI 分析 |
| ➕ 互证加分 | +0 | max +3 | 0 | 无跨数据库独立验证 |
| **原始总分** |  |  | **137/183** |  |
| **归一化总分** |  |  | **74.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | 暂无数据（Pending cell analysis），核定位基于 UniProt + GO | IF: 无可用抗体 |
| UniProt | Cytoplasm, Nucleus, Nucleolus, Midbody | 实验验证 (ECO) |

**结论**: ALKBH4 在 UniProt 中标注为核仁蛋白，具有 DNA 去甲基化酶活性。但同时定位于胞质和中体（midbody），其最主要的功能是在胞质分裂中通过去甲基化 actin K84me1 调控 actomyosin。核定位有 Nucleolus 证据，但非专一核蛋白。核定位特异性得分 6（核+显著胞质，核部分有功能性证据）。

#### 3.2 蛋白大小评估
**评价**: 302 aa，处于 200–800 aa 最优区间，适合生化实验和结构解析。

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 14 |
| 最早发表年份 | 2012 |
| Chromatin/epigenetics 比例 | 低（主要为肿瘤相关和酶学功能） |

**主要研究方向**:
- 肿瘤发生与预后（非小细胞肺癌、肝细胞癌等）
- Actin 去甲基化与胞质分裂
- DNA N6-methyladenine 去甲基化酶活性

**关键文献**:
1. Chen JL et al. (2025). "ALKBH4 functions as a hypoxia-responsive tumor suppressor and inhibits metastasis and tumorigenesis". *Cell Oncol (Dordr)*. PMID: 39400679
2. Jingushi K et al. (2021). "ALKBH4 promotes tumourigenesis with a poor prognosis in non-small-cell lung cancer". *Sci Rep*. PMID: 33883577
3. Kogaki T et al. (2023). "ALKBH4 is a novel enzyme that promotes translation through modified uridine regulation". *J Biol Chem*. PMID: 37507018
4. Cui YH et al. (2022). "ALKBH4 Stabilization Is Required for Arsenic-Induced 6mA DNA Methylation Inhibition, Keratinocyte Malignant Transformation, and Tumorigenicity". *Water (Basel)*. PMID: 37207134
5. Yu K et al. (2022). "Quantitative proteomics revealed new functions of ALKBH4". *Proteomics*. PMID: 34951099

**评价**: 14 篇文献，极度新颖。研究集中于肿瘤生物学和酶活性表征，尚无染色质/表观遗传调控的系统性研究。6mA DNA 去甲基化功能提示可能的表观遗传角色，但未被充分探索。

#### 3.4 三维结构分析
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 89.4 |
| 有序区域 (pLDDT>70) 占比 | 87% |
| pLDDT > 90 占比 | 76% |
| pLDDT < 50 占比 | 6% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ALKBH4/ALKBH4-PAE.png]]

**评价**: AlphaFold 预测质量极高（均值 89.4，87% 残基 pLDDT >70）。N 端约 50 aa 相对灵活（含 actin-binding 区），C 端 Fe2OG dioxygenase 折叠域（aa 150–274）pLDDT >95，结构极为可信。无实验 PDB 结构。结构得分 8（AlphaFold 高质量）。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt | Fe2OG dioxygenase (150–274) |
| InterPro/Pfam | IPR027450 Alpha-ketoglutarate-dependent dioxygenase AlkB-like |

**染色质调控潜力分析**: ALKBH4 含 Fe2OG dioxygenase 结构域，属于 AlkB 家族去甲基化酶。该家族成员（如 ALKBH1、ALKBH5、FTO）多参与核酸去甲基化（DNA/RNA）。ALKBH4 具有 broad specificity oxidative DNA demethylase 活性（GO ISS），且含 DNA N6-methyladenine demethylase 活性注释。但主要底物为 actin K84me1，染色质去甲基化功能尚未直接验证。结构域得分 7（新颖基线，无染色质特异性域）。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| TRAF4 | two-hybrid array | 31515488 | 信号转导 | 否 |
| EP300 | — | — | 组蛋白乙酰转移酶 | 是 |
| DTX2 | — | — | 泛素连接酶 | 否 |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ALKBH1 | 0.955 | DNA/RNA 去甲基化酶 | 是 (DNA demethylation) |
| JMJD4 | 0.896 | 去甲基化酶 | 是 |
| ALKBH7 | 0.865 | 去甲基化酶 | 否 |
| ALKBH6 | 0.860 | 去甲基化酶 | 否 |
| ALKBH2 | 0.769 | DNA 修复去甲基化酶 | 是 |
| ALKBH8 | 0.763 | tRNA 修饰酶 | 否 |
| ALKBH3 | 0.669 | RNA 去甲基化酶 | 否 |
| METTL4 | 0.669 | DNA 甲基转移酶 | 是 |
| N6AMT1 | 0.668 | 甲基转移酶 | 否 |
| APEX1 | 0.638 | DNA 修复 | 是 |
| EP300 | 0.535 | 组蛋白乙酰转移酶 | 是 |
| DTX2 | 0.514 | 泛素连接酶 (exp=0.508) | 否 |

**已知复合体成员** (GO Cellular Component):
- GO:0005730 nucleolus (IEA)
- 无染色质调控复合体注释

**PPI 互证分析**:
- STRING + IntAct 共同确认: DTX2, EP300
- 仅 STRING 预测: ALKBH 家族成员 (textmining)
- 仅 IntAct 实验: 9 个 from two-hybrid screen
- 调控相关比例: 5/14 (36%)

**评价**: PPI 网络以 ALKBH 家族互作为主，主要依赖 textmining（共提及）。EP300 是重要的染色质调控因子（组蛋白乙酰转移酶 p300），有弱实验证据 (STRING exp=0.23)。11 个 IntAct 物理互作均来自酵母双杂交筛选 (Fragoza et al. 2019)，未经验证性实验确认。PPI 得分 4（STRING >0.7 但以 textmining 为主，邻居部分调控）。
##### PPI 数据源补充核查（自动审计）

**IntAct/BioGrid 实验互作核查**:
| Partner | 方法 | PMID |
|---------|------|------|
| — | two hybrid array | 31515488 |
| — | two hybrid array | 31515488 |
| — | two hybrid prey pooling approach | 32296183 |
| — | two hybrid prey pooling approach | 32296183 |
| — | two hybrid array | 32296183 |
| — | two hybrid array | 32296183 |
| — | two hybrid array | 32296183 |
| — | validated two hybrid | 32296183 |
| — | validated two hybrid | 25416956 |
| — | two hybrid | 23145062 |

**STRING 预测/整合互作核查**:
| Partner | Score |
|---------|-------|
| ALKBH1 | 0.955 |
| JMJD4 | 0.896 |
| ALKBH7 | 0.865 |
| ALKBH6 | 0.860 |
| ALKBH2 | 0.769 |
| ALKBH8 | 0.763 |
| ALKBH3 | 0.669 |
| METTL4 | 0.669 |
| N6AMT1 | 0.668 |
| APEX1 | 0.638 |

**GO-CC 复合体/定位核查**:
- GO:0070938: contractile ring (IDA:UniProtKB)
- GO:0005737: cytoplasm (IEA:UniProtKB-SubCell)
- GO:0030496: midbody (IDA:UniProtKB)
- GO:0005730: nucleolus (IEA:UniProtKB-SubCell)

**补充结论**: PPI 评分仍以报告评分表为准；本节用于补齐 IntAct、STRING、GO-CC 三源审计证据。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT | 均值 89.4，高质量，无 PDB | — |
| 结构域 | UniProt / InterPro | Fe2OG dioxygenase (AlkB-like) | 一致 |
| PPI | STRING + IntAct | ALKBH 家族 + EP300 | — |
| 定位 | UniProt / GO | Nucleus + Nucleolus / Cytoplasm | 部分一致 |

**互证加分明细**:
- 无独立多库互证
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 极度新颖（PubMed 14 篇），几乎未被深入研究
2. 核仁定位 + DNA 去甲基化酶活性，提示表观遗传调控潜力
3. AlphaFold 结构质量极高（pLDDT 均值 89.4），结构研究可行

**风险/不确定性**:
1. 主要底物为 actin，染色质去甲基化功能尚未直接验证
2. 胞质+中体定位明显，非专一核蛋白
3. PPI 网络依赖 textmining，实验互作缺乏验证

**下一步建议**:
- [ ] 实验验证核仁定位和潜在的组蛋白/染色质去甲基化活性
- [ ] 通过 co-IP 验证与 EP300 的相互作用

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=ALKBH4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160993
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ALKBH4%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXW9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXW9

![[ALKBH4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/ALKBH4/ALKBH4-PAE.png]]
