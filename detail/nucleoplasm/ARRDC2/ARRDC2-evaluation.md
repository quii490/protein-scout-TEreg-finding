---
type: protein-evaluation
gene: "ARRDC2"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARRDC2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ARRDC2 / Arrestin domain-containing protein 2 |
| 蛋白大小 | 407 aa / 44.4 kDa |
| UniProt ID | Q8TBH0 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA IF Approved: Nucleoplasm (main); 2种抗体, 5/6组合核质确认 |
| 蛋白大小 | 10/10 | ×1 | 10 | 407 aa (200-800 aa，适合生化实验) |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed 15篇，极度新颖 |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT 81.81 (mean), 76.9% >70, 无PDB |
| 调控结构域 | 7/10 | ×2 | 14 | Arrestin_N + Arrestin_C domains, baseline |
| PPI 网络 | 3/10 | ×3 | 9 | IntAct 10条, GO-CC cytoplasm/vesicles/plasma membrane |
| 互证加分 | — | max +3 | +0.5 | Protein Atlas 2种抗体一致确认核质 |
| **原始总分** |  |  | **139.5/183** |  |
| **归一化总分** |  |  | **76.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nucleoplasm (main, approved) | Approved |
| UniProt | GO-CC: cytoplasm, cytoplasmic vesicle, plasma membrane | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARRDC2/IF_images/MCF7_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARRDC2/IF_images/PC3_1.jpg|PC-3]]

**结论**: 主要核质定位。HPA Approved, 2 种抗体 (HPA053788 + HPA074216) 确认。5/6 抗体-细胞系组合显示核质信号，PC-3 (HPA053788) 附带微弱胞质背景。UniProt GO-CC 标注为 cytoplasm，与 HPA IF 数据存在分歧，HPA IF 为实验观测，可靠性更高。

#### 3.2 蛋白大小评估
**评价**: 407 aa, 44.4 kDa，大小非常适合生化实验。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 15 |
| 最早发表年份 | 2016 |
| Chromatin/epigenetics 比例 | 极低 |

**主要研究方向**:
- 骨骼肌萎缩与力学感知 (myotube diameter regulation)
- 骨质疏松相关转录组
- 阻塞性睡眠呼吸暂停 (sarcopenia cross-talk)
- 食物限制与下丘脑转录组
- 热应激转录组

**关键文献**:
1. Laskin GR et al. (2024). "The mechanosensitive gene arrestin domain containing 2 regulates myotube diameter with direct implications for disuse atrophy with aging". *Am J Physiol Cell Physiol*. PMID: 38314723
2. Chen D et al. (2023). "Identification of Key Osteoporosis Genes Through Comparative Analysis of Men's and Women's Osteoblast Transcriptomes". *Calcif Tissue Int*. PMID: 37878026
3. Wu P et al. (2024). "RNA-seq reveals changes in the transcriptome of the breast muscle of adult female chickens in response to heat stress". *BMC Genomics*. PMID: 39614141
4. Dardente H et al. (2022). "Impact of food restriction on the medio-basal hypothalamus of intact ewes as revealed by a large-scale transcriptomics study". *J Neuroendocrinol*. PMID: 36168278
5. Lu K et al. (2026). "Possible cross-talk between sarcopenia and obstructive sleep apnea revealed by WGCNA analysis and machine learning". *Aging Male*. PMID: 41784220

**评价**: 15 篇，极度新颖。目前研究均为转录组层面的关联分析，无直接功能研究。ARRDC2 的核定位与生物功能之间的桥梁完全未建立，niche 空间极大。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 81.81 |
| pLDDT >90 占比 | 62.9% |
| pLDDT 70-90 占比 | 14.0% |
| pLDDT <50 占比 | 15.7% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARRDC2/ARRDC2-PAE.png]]

**评价**: AlphaFold 高质量预测 (mean pLDDT 81.81)，76.9% 残基 pLDDT >70。Arrestin 折叠通常高度结构化（beta-sandwich），AlphaFold 对此类折叠的预测置信度极高。无可用 PDB 实验结构。Arrestin domain 在 beta-arrestin 家族中是经典折叠，ARRDC2 可能采用类似结构。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| UniProt InterPro | Arrestin-like_N, Arrestin-like_C, Ig_E-set |
| Pfam | Arrestin_N, Arrestin_C |
| SMART | Arrestin_C |

**染色质调控潜力分析**: Arrestin domain 是 GPCR 信号转导的负调控域，主要功能为受体脱敏和内化，与染色质/DNA 无直接关联。无已知 chromatin-binding 结构域，baseline 评分。但核质定位明确（HPA Approved），蛋白在核内的功能完全未知，存在新功能发现潜力。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

| Partner | 方法 | 功能类别 | 调控相关？ |
|---|---|---|---|
| 多个蛋白 | Two-hybrid/co-IP | 信号转导/未知 | 待定 |
| RNA/miRNA interactors | CLASH | 转录后调控 | 部分 |

**STRING 预测互作**: API 不可用。

**已知复合体成员** (GO Cellular Component):
- Cytoplasm
- Cytoplasmic vesicle
- Plasma membrane

**PPI 互证分析**:
- IntAct 实验验证: 10 条记录，质量参差
- GO-CC: 均为胞质/膜组分，与 HPA 核定位存在分歧
- 调控相关比例: 低

**评价**: PPI 数据稀少，且 GO-CC 指向胞质/膜组分，与 HPA IF 数据不一致。在新颖蛋白中，PPI 稀少是正常的。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 定位 | Protein Atlas IF vs UniProt GO-CC | Nucleoplasm vs Cytoplasm | 不一致 |
| 结构域 | UniProt / InterPro / Pfam / SMART | Arrestin 多库确认 | 一致 |

**互证加分明细**:
- Protein Atlas 2种抗体确认核质: +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: (3/5)

**核心优势**:
1. HPA Approved 核质定位，2 种抗体确认
2. 极度新颖 (15 篇)，无直接功能研究
3. AlphaFold 高质量 (81.81 mean pLDDT)
4. 大小理想 (407 aa)

**风险/不确定性**:
1. UniProt GO-CC 与 HPA IF 存在分歧 (cytoplasm vs nucleoplasm)
2. Arrestin domain 不指向染色质功能
3. PPI 数据极少，核内功能完全未知
4. 核定位与 GPCR-arrestin 生物学之间的矛盾需要解释

**下一步建议**:
- [ ] 需要独立验证核定位
- [ ] 鉴定核内互作 partners

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TBH0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105643-ARRDC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ARRDC2%22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TBH0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ARRDC2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARRDC2/ARRDC2-PAE.png]]




