---
type: protein-evaluation
gene: "CWC15"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CWC15 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CWC15 / CWC15 |
| 蛋白大小 | 229 aa / ~25.2 kDa |
| UniProt ID | Q9P013 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | UniProt Nucleus + GO spliceosome/nuclear speck，剪接体核心组分 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 229 aa，200-800 aa最优区间，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=12篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | 良好（pLDDT 74.9），62%有序 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白基线 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | 3/30调控相关partners |
| ➕ 互证加分 | — | max +3 | 0 | 多库交叉验证 |
| **原始总分** |  |  | **145/183** |  |
| **归一化总分** |  |  | **79.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | — |
| GO Cellular Component | C:catalytic step 2 spliceosome; C:mitochondrion; C:nuclear speck; C:nucleoplasm; C:nucleus; C:Prp19 complex; C:spliceosomal complex; C:U2-type catalytic step 2 spliceosome | — |
| Protein Atlas (IF) | nuclear speckles+mitochondria (Approved, CACO-2) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CWC15/IF_images/CACO-2_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CWC15/IF_images/CACO-2_2.jpg|CACO-2]]

**结论**: UniProt Nucleus + GO spliceosome/nuclear speck，剪接体核心组分

#### 3.2 蛋白大小评估
**评价**: 229 aa，200-800 aa最优区间，适合生化实验和结构解析

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 12 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 12 篇。极度新颖，几乎未被研究，是探索新型核蛋白功能的绝佳候选。

**关键文献**:
1. Li Y et al. (2025). "Causal effects of brain subregion gene expression on inflammatory bowel diseases revealed by Mendelian randomization and single cell analysis". *Sci Rep*. PMID: 40594700
2. Slane D et al. (2020). "The integral spliceosomal component CWC15 is required for development in Arabidopsis". *Sci Rep*. PMID: 32770129
3. Zhou B et al. (2024). "The spliceosome-associated protein CWC15 promotes miRNA biogenesis in Arabidopsis". *Nat Commun*. PMID: 38493158
4. Yao S et al. (2022). "Alternative Splicing: A New Therapeutic Target for Ovarian Cancer". *Technol Cancer Res Treat*. PMID: 35343831
5. Kumar A et al. (2021). "Alternate PCR assays for screening of JH1 mutation associated with embryonic death in Jersey cattle". *Mol Cell Probes*. PMID: 33279530
#### 3.4 三维结构分析
> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 74.9 |
| 有序区域 (pLDDT>70) 占比 | 62.5% |
| pLDDT>90 占比 | 29.7% |
| pLDDT<50 占比 | 14.0% |
| 可用 PDB 条目 | 33 |


**评价**: AlphaFold高质量预测（pLDDT 74.9，62%有序），折叠域置信度高。 PDB 33条条目提供实验参考。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:cwc15_yeast(display_long)|uniprotkb:CWC15(gene name)|psi-mi:CWC15(display_short)|uniprotkb:Complexed with CEF1 protein 15(gene name synonym)|uniprotkb:YDR163W(locus name)|uniprotkb:YD8358.17(orf name) | psi-mi:"MI:0397"(two hybrid ar | pubmed:15766533 | 待分析 | 否 |
| psi-mi:cef1_yeast(display_long)|uniprotkb:CEF1(gene name)|psi-mi:CEF1(display_short)|uniprotkb:YMR213W(locus name)|uniprotkb:YM8261.07(orf name)|uniprotkb:NTC85(gene name synonym)|uniprotkb:PRP nineteen-associated complex protein 85(gene name synonym)|uniprotkb:PRP19-associated complex protein 85(gene name synonym) | psi-mi:"MI:0006"(anti bait coi | pubmed:11884590 | 待分析 | 否 |
| psi-mi:cef1_yeast(display_long)|uniprotkb:CEF1(gene name)|psi-mi:CEF1(display_short)|uniprotkb:YMR213W(locus name)|uniprotkb:YM8261.07(orf name)|uniprotkb:NTC85(gene name synonym)|uniprotkb:PRP nineteen-associated complex protein 85(gene name synonym)|uniprotkb:PRP19-associated complex protein 85(gene name synonym) | psi-mi:"MI:0006"(anti bait coi | pubmed:11884590 | 待分析 | 否 |
| psi-mi:cwc15_human(display_long)|uniprotkb:CWC15(gene name)|psi-mi:CWC15(display_short)|uniprotkb:C11orf5(gene name synonym)|uniprotkb:AD-002(orf name)|uniprotkb:HSPC148(orf name) | psi-mi:"MI:0397"(two hybrid ar | imex:IM-15364|pubmed:21988832 | 待分析 | 否 |
| psi-mi:cwc15_human(display_long)|uniprotkb:CWC15(gene name)|psi-mi:CWC15(display_short)|uniprotkb:C11orf5(gene name synonym)|uniprotkb:AD-002(orf name)|uniprotkb:HSPC148(orf name) | psi-mi:"MI:0398"(two hybrid po | imex:IM-13779|pubmed:20711500 | 待分析 | 否 |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| BCAS2 | 0.999 | 待分析 | 否 |
| BUD31 | 0.999 | 待分析 | 否 |
| SNW1 | 0.999 | 待分析 | 否 |
| CTNNBL1 | 0.999 | 待分析 | 否 |
| RBM22 | 0.999 | 待分析 | 是 |
| CDC5L | 0.999 | 待分析 | 是 |
| SNRPA1 | 0.999 | 待分析 | 否 |
| CRNKL1 | 0.999 | 待分析 | 否 |
| PRPF8 | 0.999 | 待分析 | 否 |
| EFTUD2 | 0.999 | 待分析 | 否 |


**已知复合体成员** (GO Cellular Component): C:catalytic step 2 spliceosome; C:mitochondrion; C:nuclear speck; C:nucleoplasm; C:nucleus; C:Prp19 complex; C:spliceosomal complex; C:U2-type catalytic step 2 spliceosome

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: 30 个伙伴
- 调控相关比例: 3/30 (10%)

**评价**: PPI网络以功能关联为主（30个STRING伙伴），物理互作17个，调控关联3个。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 良好（pLDDT 74.9），62%有序 | 待验证 |
| 定位 | UniProt + GO | Nucleus | 待HPA验证 |

**互证加分**: 0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (4/5)

**归一化总分**: **77.6/100**

**核心优势**:
1. PubMed 12 篇，研究新颖性高
2. 蛋白大小 229 aa，适合生化实验

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P013
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P013
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CWC15%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CWC15&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CWC15


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CWC15/CWC15-PAE.png]]




