---
type: protein-evaluation
gene: "CWC27"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CWC27 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CWC27 / CWC27 |
| 蛋白大小 | 472 aa / ~51.9 kDa |
| UniProt ID | Q6UX04 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | UniProt Nucleus + GO spliceosome/nucleoplasm，剪接体组分 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 472 aa，200-800 aa最优区间，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed=26篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | 良好（pLDDT 73.6），67%有序 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白基线 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | 2/30调控相关partners |
| ➕ 互证加分 | — | max +3 | 0 | 多库交叉验证 |
| **原始总分** |  |  | **135/183** |  |
| **归一化总分** |  |  | **73.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | — |
| GO Cellular Component | C:catalytic step 2 spliceosome; C:nucleoplasm; C:U2-type precatalytic spliceosome | — |
| Protein Atlas (IF) | nucleoplasm (Approved, A-431) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CWC27/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CWC27/IF_images/A-431_2.jpg|A-431]]

**结论**: UniProt Nucleus + GO spliceosome/nucleoplasm，剪接体组分

#### 3.2 蛋白大小评估
**评价**: 472 aa，200-800 aa最优区间，适合生化实验和结构解析

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 26 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 26 篇。非常新颖，研究空间充足。

**关键文献**:
1. Rajiv C & Davis TL (2018). "Structural and Functional Insights into Human Nuclear Cyclophilins". *Biomolecules*. PMID: 30518120
2. Fang K et al. (2025). "Regulation of tau protein by circCwc27: shared pathogenic mechanisms in type 2 diabetes mellitus and Alzheimer's disease". *Brain Inform*. PMID: 41037159
3. Beauchamp MC et al. (2020). "Spliceosomopathies and neurocristopathies: Two sides of the same coin?". *Dev Dyn*. PMID: 32315467
4. Shen X et al. (2022). "Role of circRNA in pathogenesis of Alzheimer's disease". *Zhong Nan Da Xue Xue Bao Yi Xue Ban*. PMID: 36039594
5. Lu J et al. (2023). "Gene augmentation therapy to rescue degenerative photoreceptors in a Cwc27 mutant mouse model". *Exp Eye Res*. PMID: 37479075
#### 3.4 三维结构分析
> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 73.6 |
| 有序区域 (pLDDT>70) 占比 | 67.4% |
| pLDDT>90 占比 | 26.5% |
| pLDDT<50 占比 | 16.9% |
| 可用 PDB 条目 | 9 |


**评价**: AlphaFold高质量预测（pLDDT 73.6，67%有序），折叠域置信度高。 PDB 9条条目提供实验参考。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:e2f1_human(display_long)|uniprotkb:Retinoblastoma-associated protein 1(gene name synonym)|uniprotkb:Retinoblastoma-binding protein 3(gene name synonym)|uniprotkb:PBR3(gene name synonym)|uniprotkb:E2F1(gene name)|psi-mi:E2F1(display_short)|uniprotkb:RBBP3(gene name synonym)|uniprotkb:pRB-binding protein E2F-1(gene name synonym) | psi-mi:"MI:0034"(display techn | pubmed:20195357|imex:IM-20475 | 待分析 | 是 |
| psi-mi:q9vtn7_drome(display_long)|uniprotkb:Dmel\CG10907(gene name)|psi-mi:Dmel\CG10907(display_short)|uniprotkb:Probable inactive peptidyl-prolyl cis-trans isomerase CWC27 homolog(gene name synonym)|uniprotkb:CG10907(orf name)|uniprotkb:Dmel_CG10907(orf name) | psi-mi:"MI:0397"(two hybrid ar | pubmed:37061542|imex:IM-28761 | 待分析 | 否 |
| psi-mi:q9vtn7_drome(display_long)|uniprotkb:Dmel\CG10907(gene name)|psi-mi:Dmel\CG10907(display_short)|uniprotkb:Probable inactive peptidyl-prolyl cis-trans isomerase CWC27 homolog(gene name synonym)|uniprotkb:CG10907(orf name)|uniprotkb:Dmel_CG10907(orf name) | psi-mi:"MI:1112"(two hybrid pr | pubmed:37061542|imex:IM-28761 | 待分析 | 否 |
| psi-mi:q6ux042(display_long)|uniprotkb:CWC27(gene name)|psi-mi:CWC27(display_short)|uniprotkb:SDCCAG10(gene name synonym)|uniprotkb:UNQ438/PRO871(orf name) | psi-mi:"MI:1112"(two hybrid pr | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:q6ux042(display_long)|uniprotkb:CWC27(gene name)|psi-mi:CWC27(display_short)|uniprotkb:SDCCAG10(gene name synonym)|uniprotkb:UNQ438/PRO871(orf name) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| SNRNP200 | 0.999 | 待分析 | 否 |
| RNF113A | 0.999 | 待分析 | 否 |
| CWC22 | 0.999 | 待分析 | 否 |
| DHX16 | 0.998 | 待分析 | 否 |
| SNIP1 | 0.997 | 待分析 | 否 |
| BUD13 | 0.997 | 待分析 | 否 |
| CDC5L | 0.997 | 待分析 | 是 |
| SNRPA1 | 0.997 | 待分析 | 否 |
| PRPF8 | 0.997 | 待分析 | 否 |
| RBMX2 | 0.997 | 待分析 | 是 |


**已知复合体成员** (GO Cellular Component): C:catalytic step 2 spliceosome; C:nucleoplasm; C:U2-type precatalytic spliceosome

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: 30 个伙伴
- 调控相关比例: 2/30 (7%)

**评价**: PPI网络以功能关联为主（30个STRING伙伴），物理互作6个，调控关联2个。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 良好（pLDDT 73.6），67%有序 | 待验证 |
| 定位 | UniProt + GO | Nucleus | 待HPA验证 |

**互证加分**: 0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**归一化总分**: **72.1/100**

**核心优势**:
1. PubMed 26 篇，研究新颖性高
2. 蛋白大小 472 aa，适合生化实验

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UX04
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UX04
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CWC27%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CWC27&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CWC27


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CWC27/CWC27-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6UX04 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 11..166; /note="PPIase cyclophilin-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00156" |
| InterPro | IPR029000;IPR020892;IPR002130;IPR044666; |
| Pfam | PF00160; |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
