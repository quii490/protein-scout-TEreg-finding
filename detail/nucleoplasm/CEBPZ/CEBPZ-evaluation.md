---
type: protein-evaluation
gene: "CEBPZ"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CEBPZ 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEBPZ / CEBPZ |
| 蛋白大小 | 1054 aa / ~115.9 kDa |
| UniProt ID | Q03701 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | UniProt Nucleus + GO CCAAT-binding/nucleoplasm，CCAAT结合转录因子 |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 1054 aa，偏大但可操作 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed=30篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | 中等（pLDDT 67.0），55%有序，31%无序 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白基线 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | 2/30调控相关partners |
| ➕ 互证加分 | — | max +3 | 0 | 多库交叉验证 |
| **原始总分** |  |  | **130/183** |  |
| **归一化总分** |  |  | **71.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | — |
| GO Cellular Component | C:CCAAT-binding factor complex; C:nucleoplasm; C:nucleus | — |
| Protein Atlas (IF) | nucleoplasm+vesicles (Approved, HeLa) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CEBPZ/IF_images/783_H4_1_red_green.jpg|HPA IF]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CEBPZ/IF_images/868_E12_1_red_green.jpg|868_E12_1_red_green]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CEBPZ/IF_images/785_H4_6_red_green.jpg|HPA IF]]


**结论**: UniProt Nucleus + GO CCAAT-binding/nucleoplasm，CCAAT结合转录因子

#### 3.2 蛋白大小评估
**评价**: 1054 aa，偏大但可操作

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 30 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 30 篇。非常新颖，研究空间充足。

**关键文献**:
1. Barbieri I et al. (2017). "Promoter-bound METTL3 maintains myeloid leukaemia by m(6)A-dependent translation control". *Nature*. PMID: 29186125
2. Chen S et al. (2025). "Baicalein Induces Hepatic Stellate Cell Senescence and Attenuates Liver Fibrosis via CEBPZ/p53/HK2-Mediated Glycolysis Inhibition". *Phytomedicine*. PMID: 41075517
3. Duan P et al. (2024). "Exosomal miR-1a-3p derived from glucocorticoid-stimulated M1 macrophages promotes the adipogenic differentiation of BMSCs in glucocorticoid-associated osteonecrosis of the femoral head by targeting...". *J Nanobiotechnology*. PMID: 39438865
4. Alhosani F et al. (2025). "Transcriptome-Wide Analysis and Experimental Validation from FFPE Tissue Identifies Stage-Specific Gene Expression Profiles Differentiating Adenoma, Carcinoma In-Situ and Adenocarcinoma in Colorect...". *Int J Mol Sci*. PMID: 40362431
5. Mao T et al. (2025). "DNAJC9 Binds to and Enhances the Transcription of Hepatitis B Virus cccDNA by Recruiting Histone H3.3". *J Med Virol*. PMID: 40407066
#### 3.4 三维结构分析
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 67.0 |
| 有序区域 (pLDDT>70) 占比 | 55.2% |
| pLDDT>90 占比 | 15.5% |
| pLDDT<50 占比 | 31.0% |
| 可用 PDB 条目 | 0 |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CEBPZ/CEBPZ-PAE.png]]


**评价**: AlphaFold中等质量（pLDDT 67.0，55%有序）。作为新颖蛋白（PubMed=30），此结构水平可接受（基线6分）。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:h14_human(display_long)|uniprotkb:H1-4(gene name)|psi-mi:H1-4(display_short)|uniprotkb:H1F4(gene name synonym)|uniprotkb:HIST1H1E(gene name synonym)|uniprotkb:Histone H1b(gene name synonym)|uniprotkb:Histone H1s-4(gene name synonym) | psi-mi:"MI:0030"(cross-linking | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 | 待分析 | 是 |
| psi-mi:cebpz_human(display_long)|uniprotkb:CCAAT-box-binding transcription factor(gene name synonym)|uniprotkb:CEBPZ(gene name)|psi-mi:CEBPZ(display_short)|uniprotkb:CBF2(gene name synonym) | psi-mi:"MI:0006"(anti bait coi | pubmed:17353931 | 待分析 | 是 |
| psi-mi:pebb_human(display_long)|uniprotkb:Polyomavirus enhancer-binding protein 2 beta subunit(gene name synonym)|uniprotkb:SL3-3 enhancer factor 1 subunit beta(gene name synonym)|uniprotkb:SL3/AKV core-binding factor beta subunit(gene name synonym)|uniprotkb:CBFB(gene name)|psi-mi:CBFB(display_short) | psi-mi:"MI:0034"(display techn | pubmed:20195357|imex:IM-20475 | 待分析 | 否 |
| psi-mi:cebpz_mouse(display_long)|uniprotkb:Cebpz(gene name)|psi-mi:Cebpz(display_short)|uniprotkb:Cbf2(gene name synonym)|uniprotkb:Cebpa-rs1(gene name synonym)|uniprotkb:CCAAT-box-binding transcription factor(gene name synonym) | psi-mi:"MI:0018"(two hybrid) | pubmed:14611647|imex:IM-16925 | 待分析 | 是 |
| psi-mi:sufu_mouse(display_long)|uniprotkb:Sufu(gene name)|psi-mi:Sufu(display_short) | psi-mi:"MI:0018"(two hybrid) | pubmed:14611647|imex:IM-16925 | 待分析 | 否 |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| NOC2L | 0.999 | 待分析 | 否 |
| PDCD11 | 0.999 | 待分析 | 否 |
| RBM28 | 0.984 | 待分析 | 是 |
| GTPBP4 | 0.983 | 待分析 | 否 |
| DDX56 | 0.979 | 待分析 | 否 |
| MPHOSPH10 | 0.977 | 待分析 | 否 |
| RPF2 | 0.975 | 待分析 | 否 |
| RRP12 | 0.972 | 待分析 | 否 |
| PUM3 | 0.972 | 待分析 | 否 |
| UTP20 | 0.968 | 待分析 | 否 |


**已知复合体成员** (GO Cellular Component): C:CCAAT-binding factor complex; C:nucleoplasm; C:nucleus

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: 30 个伙伴
- 调控相关比例: 2/30 (7%)

**评价**: PPI网络以功能关联为主（30个STRING伙伴），物理互作13个，调控关联2个。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 中等（pLDDT 67.0），55%有序，31%无序 | 待验证 |
| 定位 | UniProt + GO | Nucleus | 待HPA验证 |

**互证加分**: 0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**归一化总分**: **69.4/100**

**核心优势**:
1. PubMed 30 篇，研究新颖性高
2. 蛋白大小 1054 aa

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q03701
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q03701
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CEBPZ%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CEBPZ&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CEBPZ


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[CEBPZ-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CEBPZ/CEBPZ-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q03701 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR016024;IPR005612;IPR040155; |
| Pfam | PF03914; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000115816-CEBPZ/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GSK3B | Intact, Biogrid | true |
| PRKRA | Intact, Biogrid, Bioplex | true |
| RRP8 | Biogrid, Bioplex | true |
| TP53 | Intact, Biogrid | true |
| ADARB1 | Biogrid | false |
| ANLN | Biogrid | false |
| APEX1 | Biogrid | false |
| FBL | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
