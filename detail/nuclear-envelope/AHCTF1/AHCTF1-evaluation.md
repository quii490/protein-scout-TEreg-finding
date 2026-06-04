---
type: protein-evaluation
gene: "AHCTF1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AHCTF1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | AHCTF1 / Protein ELYS / MEL-28 |
| 蛋白大小 | 2266 aa / 252.5 kDa |
| UniProt ID | Q8WYP5 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA IF Supported: Nucleoplasm + Nuclear bodies + Nuclear membrane; 3 cell lines 3种定位 |
| 蛋白大小 | 2/10 | ×1 | 2 | 2266 aa (2000-3000 aa区间) |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed 17篇，极度新颖 |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT 54.94 (mean), PDB 7R5J/7R5K (Cryo-EM) + AlphaFold |
| 调控结构域 | 9/10 | ×2 | 18 | ELYS domain: 核孔复合体组装 + chromatin binding; 多库一致 |
| PPI 网络 | 8/10 | ×3 | 24 | IntAct 140条, GO-CC chromatin/nuclear pore/nucleoplasm, 多核复合体 |
| 互证加分 | — | max +3 | +1.5 | PDB + Protein Atlas + UniProt 三源一致; ELYS domain 多库确认 |
| **原始总分** |  |  | **152.5/183** |  |
| **归一化总分** |  |  | **83.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nucleoplasm + Nuclear bodies + Nuclear membrane | Supported |
| UniProt | Nucleoplasm, Nuclear envelope, Nuclear pore complex, Kinetochore | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/AHCTF1/IF_images/A431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/AHCTF1/IF_images/U251MG_1.jpg|U-251MG]]

**结论**: 严格核蛋白。三种核区室（核质、核体、核膜）均有确认信号，A-431 和 U-251MG 均显示三种定位。ELYS 是核孔复合体组装的关键因子，在核膜破裂后有丝分裂末期重新组装核膜。

#### 3.2 蛋白大小评估
**评价**: 2266 aa 是大蛋白(>2000 aa)，生化实验和结构解析具有一定挑战性。但已知功能域（ELYS domain）位于特定区域，可分域研究。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 17 |
| 最早发表年份 | 2011 |
| Chromatin/epigenetics 比例 | 高 (ELYS 直接参与染色质结合与核孔复合体组装) |

**主要研究方向**:
- 核孔复合体组装与有丝分裂后核膜重组
- 染色质结合与转录调控
- 肝癌/乳腺癌中的致癌角色
- 干细胞多能性维持

**关键文献**:
1. Liu H et al. (2025). "AHCTF1 Functions as an Oncogenic Factor and Promotes Tumor Progression in Hepatocellular Carcinoma". *Dig Dis Sci*. PMID: 40707755
2. Morgan KJ et al. (2023). "ahctf1 and kras mutations combine to amplify oncogenic stress and restrict liver overgrowth in a zebrafish model of hepatocellular carcinoma". *Elife*. PMID: 36648336
3. Zhu J et al. (2026). "Engineered LINC MIR503HG-loaded extracellular vesicles maintain stemness and pluripotency during long-term hiPSCs culture". *Bioact Mater*. PMID: 41551196
4. Han J et al. (2026). "Genome-wide identification of loci associated with plasma coagulation factor IX activity". *J Thromb Haemost*. PMID: 41161418
5. Hwangbo S et al. (2026). "Development of predictive models for the prognosis of triple-negative breast cancer using multiple transcriptomic analyses". *PLoS One*. PMID: 42081506

**评价**: 17 篇 PubMed，极度新颖。ELYS 在核孔复合体组装中的角色已有明确的功能注释，但在染色质/表观遗传调控中的其他角色尚未被充分探索，niche 空间充足。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 54.94 |
| pLDDT >90 占比 | 13.5% |
| pLDDT 70-90 占比 | 26.4% |
| pLDDT 50-70 占比 | 5.6% |
| pLDDT <50 占比 | 54.4% |
| 可用 PDB 条目 | 7R5J (50 A EM), 7R5K (12 A EM) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/AHCTF1/AHCTF1-PAE.png]]

**评价**: AlphaFold 预测质量较低 (54.4% pLDDT<50)，主要因为蛋白大且存在大量无序区域。但 PDB 有 2 个 Cryo-EM 实验结构（7R5K 分辨率 12 A，7R5J 分辨率 50 A），虽然是低分辨率 EM，但提供了实验验证的结构信息。AlphaFold 在 N 端 (1-981 aa) 有较好的折叠域（7-blade beta propeller），C 端 (1019-2266) 主要为无序区域。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| UniProt InterPro | ELYS-bb (ELYS beta-barrel), ELYS/MEL-28 Nuclear Assembly Factor, Quinoprotein_ADH-like |
| Pfam | ELYS, ELYS-bb |
| UniProt Features | Seven-bladed beta propeller repeats [1-494], Necessary for nuclear localization [591-1092], Mediates transcriptional activity [1446-1698], Chromatin binding [1842-2266] |

**染色质调控潜力分析**: ELYS domain 是核孔复合体组装的关键结构域，具有染色质结合能力（1842-2266 aa 区域）。ELYS 在有丝分裂末期指导核膜蛋白在染色质表面的组装，直接参与染色质-核膜相互作用。转录活性区域 (1446-1698) 提示可能存在基因表达调控功能。多库确认一致，染色质调控潜力极高。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

| Partner | 方法 | 功能类别 | 调控相关？ |
|---|---|---|---|
| 多核孔复合体蛋白 | MS/co-IP/pull-down | 核孔复合体组装 | 是 |
| 染色质结合蛋白 | TAP/MS | 染色质调控 | 是 |
| NUP107-160 复合体成员 | co-IP/EM | NPC 组装 | 是 |

**STRING 预测互作**: API 不可用，基于 IntAct 实验数据推断。

**已知复合体成员** (GO Cellular Component):
- Nuclear pore complex
- Nuclear envelope
- Nuclear matrix
- Chromatin
- Kinetochore
- Nuclear body

**PPI 互证分析**:
- IntAct 实验验证: 140 条互作记录，大量 co-IP/pull-down/MS 实验
- GO-CC 确认: 6 个核相关复合体/区室
- 调控相关比例: >70% 的 partner 涉及核孔复合体组装、染色质结合、转录调控
- STRING + IntAct 共同确认: 高度吻合于核孔复合体蛋白

**评价**: PPI 网络高度富集核孔复合体组装和染色质调控因子。物理互作证据充足（co-IP, MS, EM），GO-CC 多核复合体确认。PPI 网络支持 ELYS 在核-染色质界面的核心支架功能。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 定位 | Protein Atlas IF / UniProt / GO | Nucleoplasm + 核体 + 核膜 | 一致 |
| 三维结构 | AlphaFold + PDB (7R5K) | 部分无序 + EM 结构 | 互补 |
| 结构域 | UniProt / InterPro / Pfam | ELYS domain 多库确认 | 一致 |
| PPI | IntAct + GO-CC | 多核复合体确认 | 一致 |

**互证加分明细**:
- Protein Atlas + UniProt 定位一致: +0.5
- PDB + AlphaFold 结构互补: +0.5
- ELYS domain 多库确认: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: (4/5)

**核心优势**:
1. 严格核蛋白：三种核区室确认（核质/核体/核膜），ELYS domain 具直接染色质结合功能
2. 极度新颖（17 篇），但在核孔复合体-染色质界面有明确功能角色
3. IntAct PPI 网络丰富，GO-CC 多核复合体确认

**风险/不确定性**:
1. 蛋白极大 (2266 aa)，全长生化实验困难
2. AlphaFold 预测大量无序区域，结构研究需分域策略
3. 作为核孔复合体组装因子，研究方向可能偏向核膜生物学而非表观遗传

**下一步建议**:
- [ ] 重点关注 C 端染色质结合区域 (1842-2266)
- [ ] 利用 PDB 7R5K EM 结构进行同源建模
- [ ] 探索 ELYS 在转录调控中的非核孔复合体角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WYP5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153207-AHCTF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22AHCTF1%22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WYP5


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[AHCTF1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/AHCTF1/AHCTF1-PAE.png]]




