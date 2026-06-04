---
type: protein-evaluation
gene: "CYB561A3"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CYB561A3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYB561A3 / CYB561A3 |
| 蛋白大小 | 242 aa / ~26.6 kDa |
| UniProt ID | Q8NBI2 |
| 评估日期 | 2026-05-29 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CYB561A3/IF_images/HaCaT_1.jpg|HaCaT]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CYB561A3/IF_images/SiHa_1.jpg|SiHa]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | UniProt Late endosome/lysosome membrane，GO nucleolus次要，主要定位非核 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 242 aa，200-800 aa最优区间，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=4篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | 高质量（pLDDT 92.3），93%有序 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白基线 |
| 🔗 PPI 网络 | 2/10 | ×3 | 6 | 0/1调控相关partners |
| ➕ 互证加分 | — | max +3 | 0 | 多库交叉验证 |
| **原始总分** |  |  | **123/183** |  |
| **归一化总分** |  |  | **67.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Late endosome membrane; Lysosome membrane | — |
| GO Cellular Component | C:late endosome membrane; C:lysosomal membrane; C:nucleolus | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。


暂无数据（HPA IF 图像已本地嵌入。


**结论**: UniProt Late endosome/lysosome membrane，GO nucleolus次要，主要定位非核

#### 3.2 蛋白大小评估
**评价**: 242 aa，200-800 aa最优区间，适合生化实验和结构解析

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 4 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 4 篇。极度新颖，几乎未被研究，是探索新型核蛋白功能的绝佳候选。

**关键文献**:
1. Feng Y et al. (2024). "Integrative functional genomic analyses identify genetic variants influencing skin pigmentation in Africans". *Nat Genet*. PMID: 38200130
2. Meng F et al. (2022). "Lysosomal iron recycling in mouse macrophages is dependent upon both LcytB and Steap3 reductases". *Blood Adv*. PMID: 34982827
3. Al-Eitan LN et al. (2020). "Transcriptome analysis of HPV-induced warts and healthy skin in humans". *BMC Med Genomics*. PMID: 32151264
4. Wang X et al. (2024). "RNA-Seq Profiling in Chicken Spleen and Thymus Infected with Newcastle Disease Virus of Varying Virulence". *Vet Sci*. PMID: 39591343
5. Wang Z et al. (2021). "CYB561A3 is the key lysosomal iron reductase required for Burkitt B-cell growth and survival". *Blood*. PMID: 34232987
#### 3.4 三维结构分析
> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 92.3 |
| 有序区域 (pLDDT>70) 占比 | 92.6% |
| pLDDT>90 占比 | 83.5% |
| pLDDT<50 占比 | 5.0% |
| 可用 PDB 条目 | 0 |


**评价**: AlphaFold高质量预测（pLDDT 92.3，93%有序），折叠域置信度高。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:t4s18_human(display_long)|uniprotkb:TM4SF18(gene name)|psi-mi:TM4SF18(display_short) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:shsl1_human(display_long)|uniprotkb:SHISAL1(gene name)|psi-mi:SHISAL1(display_short)|uniprotkb:KIAA1644(gene name synonym) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:lap4b_human(display_long)|uniprotkb:LAPTM4B(gene name)|psi-mi:LAPTM4B(display_short)|uniprotkb:Lysosome-associated transmembrane protein 4-beta(gene name synonym)|uniprotkb:PSEC0001(orf name) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:cld7_human(display_long)|uniprotkb:CLDN7(gene name)|psi-mi:CLDN7(display_short)|uniprotkb:CEPTRL2(gene name synonym)|uniprotkb:CPETRL2(gene name synonym) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:cyac3_human(display_long)|uniprotkb:CYB561A3(gene name)|psi-mi:CYB561A3(display_short)|uniprotkb:CYBASC3(gene name synonym)|uniprotkb:Cytochrome b561 family member A3(gene name synonym)|uniprotkb:Lysosomal cytochrome b(gene name synonym)|uniprotkb:PSEC0259(orf name)|uniprotkb:Cytochrome b ascorbate-dependent protein 3(gene name synonym) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 是 |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component): C:late endosome membrane; C:lysosomal membrane; C:nucleolus

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: 0 个伙伴
- 调控相关比例: 0/1 (0%)

**评价**: PPI网络稀薄，调控关联极少（0/1），可能为独立功能蛋白。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 高质量（pLDDT 92.3），93%有序 | 待验证 |
| 定位 | UniProt + GO | Late endosome membrane; Lysosome membrane | 待HPA验证 |

**互证加分**: 0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**归一化总分**: **65.6/100**

**核心优势**:
1. PubMed 4 篇，研究新颖性高
2. 蛋白大小 242 aa，适合生化实验

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NBI2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NBI2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CYB561A3%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CYB561A3&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CYB561A3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CYB561A3/CYB561A3-PAE.png]]


