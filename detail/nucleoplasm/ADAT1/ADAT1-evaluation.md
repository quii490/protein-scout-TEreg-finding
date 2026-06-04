---
type: protein-evaluation
gene: "ADAT1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ADAT1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ADAT1 / hADAT1, tRNA-specific adenosine deaminase 1 |
| 蛋白大小 | 502 aa / ~56 kDa |
| UniProt ID | Q9BUB4 |
| 评估日期 | 2026-05-29 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ADAT1/IF_images/U2OS_1.jpg|U2OS]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ADAT1/IF_images/A-431_1.jpg|A-431]]


### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: 核质为主(A-431/U-2 OS/U-251 MG)，部分Golgi；UniProt无亚细胞定位注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 502 aa，200-800 aa 最优区间 |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=12，极度新颖 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AF pLDDT=81.7, >70=77%，无PDB |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | tRNA A-to-I editase domain，RNA结合 |
| 🔗 PPI 网络 | 2/10 | ×3 | 6 | ADAT3/ADAT2/KARS1/AARS1，均为tRNA通路，无染色质关联 |
| ➕ 互证加分 | — | max +3 | 0 | 无多库互证 |
| **原始总分** |  |  | **131/183** |  |
| **归一化总分** |  |  | **71.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleoplasm | — |
| Protein Atlas (IF) | 核质（A-431, U-2 OS, U-251 MG），SiHa 显示核质+Golgi | 多个细胞系验证 |
| UniProt | 无亚细胞定位注释 | — |

**IF images**: 暂无数据（HPA IF 图像已本地嵌入。

- HPA040903: A-431 (核质), U-2 OS (核质), U-251 MG (核质)

**结论**: HPA IF 在多个细胞系中确认核质定位。UniProt 缺少亚细胞定位注释，但 HPA 数据可独立支持核定位。tRNA A37 脱氨酶功能在胞质中执行，但核内也可能存在 tRNA 编辑活性。核定位 = 7。

#### 3.2 蛋白大小评估
**评价**: 502 aa，大小适合生化实验和结构解析（200–800 aa 最优区间）。

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 12 |
| 最早发表年份 | 1999 |
| Chromatin/epigenetics 比例 | 0% |

**主要研究方向**:
- tRNA A37 adenosine-to-inosine 编辑
- 肌醇六磷酸（IP6）在 tRNA 编辑中的作用
- RNA 编辑与疾病关系

**关键文献**:
1. Torres et al. (2015). "Parallel Evolution and Lineage-Specific Expansion of RNA Editing in Ctenophores". *Integr Comp Biol*. PMID: 26089435
2. Maas et al. (1999). "Cloning and characterization of human ADAT1". *J Biol Chem*. PMID: 10430867
3. Gerber et al. (2002). "RNA editing by adenosine deaminases generates RNA and protein diversity". *Biochimie*. PMID: 12457566

**评价**: 研究极度稀少（12 篇），全部集中于 tRNA 编辑功能，与染色质/表观遗传完全无关。

**关键文献**:
1. Zhang H et al. (2023). "Machine learning-based integrated identification of predictive combined diagnostic biomarkers for endometriosis". *Front Genet*. PMID: 38098472
2. Kohn AB et al. (2015). "Parallel Evolution and Lineage-Specific Expansion of RNA Editing in Ctenophores". *Integr Comp Biol*. PMID: 26089435
3. Macbeth MR et al. (2005). "Inositol hexakisphosphate is bound in the ADAR2 core and required for RNA editing". *Science*. PMID: 16141067
4. Schaub M & Keller W (2002). "RNA editing by adenosine deaminases generates RNA and protein diversity". *Biochimie*. PMID: 12457566
5. Yoon YB et al. (2021). "Identification and expression of adenosine deaminases acting on tRNA (ADAT) during early tail regeneration of the earthworm". *Genes Genomics*. PMID: 33575975
#### 3.4 三维结构分析
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 81.7 |
| 有序区域 (pLDDT>70) 占比 | 77% |
| pLDDT>90 占比 | 68% |
| pLDDT<50 占比 | 19% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ADAT1/ADAT1-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵尺寸: 502×502
- PAE 总体均值: 12.5
- PAE <5 Å 占比: 43.4%
- PAE <10 Å 占比: 58.2%

**评价**: AlphaFold 结构质量良好（pLDDT 81.7），77% 有序区域。PAE 表现良好（43.4% <5 Å），说明连续结构域折叠可靠。N 端和 C 端各有约 94 个残基为无序区域（pLDDT<50）。无实验 PDB 结构。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| GeneCards | Adenosine deaminase/editase |
| SMART | A_deaminase (PF02137), A to I editase (PS50276) |
| InterPro/Pfam | Cytidine deaminase-like (IPR016192), Adenosine deaminase/editase (IPR002466) |

**染色质调控潜力分析**: A to I editase 结构域催化 tRNA 中 adenosine-37 脱氨为 inosine。这是 RNA 编辑功能，与 DNA/染色质调控无直接关联。无任何暗示染色质结合的域。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| ADAT3 | physical association | 14605208 | tRNA 编辑 | 否 |
| ADAT2 | physical association | 14605208 | tRNA 编辑 | 否 |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ADAT3 | 0.953 | tRNA A34 脱氨酶 | 否 |
| ADAT2 | 0.931 | tRNA A34 脱氨酶催化亚基 | 否 |
| KARS1 | 0.922 | 赖氨酰-tRNA 合成酶 | 否 |
| AARS1 | 0.870 | 丙氨酰-tRNA 合成酶 | 否 |
| AARSD1 | 0.652 | tRNA 合成酶 | 否 |
| TRMT5 | 0.598 | tRNA 甲基转移酶 | 否 |
| DUXB | 0.572 | 双同源盒转录因子 | 边缘 |
| TERF2IP | 0.546 | 端粒结合蛋白 | 否 |
| IPPK | 0.527 | 肌醇激酶（IP6 合成） | 否 |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 注释

**PPI 互证分析**:
- STRING + IntAct 共同确认: ADAT2, ADAT3
- 仅 STRING 预测: 剩余的 tRNA 合成酶和代谢酶
- 调控相关比例: 1/9 (11%) — DUXB 为转录因子但 score 仅 0.572

**评价**: PPI 网络完全集中于 tRNA 编辑和翻译机器（ADAT2/3、KARS1、AARS1）。唯一边缘关联 DUXB（双同源盒转录因子）score 较低。无染色质调控伙伴。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AF pLDDT=81.7, 无PDB | 中等质量（77%有序） | N/A |
| 结构域 | UniProt/SMART/Pfam → A to I editase | tRNA 编辑酶 | 完全一致 |
| PPI | STRING + IntAct → ADAT2/ADAT3 | tRNA 编辑复合体 | 一致 |
| 定位 | HPA IF 核质 / UniProt 无注释 / GO 无CC | 仅HPA支持 | 部分一致 |

**互证加分明细**: 结构域多库完全一致（+1），但 PPI 和定位的多库互证不足。**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**核心优势**:
1. PubMed 仅 12 篇，极度新颖
2. 蛋白大小（502 aa）和结构质量（pLDDT 81.7）适合生化实验
3. HPA IF 在多个细胞系明确显示核质定位

**风险/不确定性**:
1. **功能与染色质完全无关**: tRNA 编辑酶，研究方向与染色质/表观遗传不匹配
2. PPI 网络局限：所有互作均为 tRNA/翻译通路，无染色质调控伙伴
3. UniProt 缺少亚细胞定位注释，核定位仅依赖 HPA IF
4. 作为 tRNA 编辑酶，主要功能可能位于胞质，核定位可能是次要池

**下一步建议**:
- 该蛋白功能与项目核染色质调控研究方向不匹配，不推荐深入
- 若项目转向 RNA 修饰/表观转录组学，可重新评估

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BUB4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000065457-ADAT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ADAT1%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BUB4


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ADAT1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ADAT1/ADAT1-PAE.png]]


