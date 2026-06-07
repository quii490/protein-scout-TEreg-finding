---
type: protein-evaluation
gene: "CHP2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CHP2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHP2 / Calcineurin B homologous protein 2 |
| 蛋白大小 | 196 aa / 22.5 kDa |
| UniProt ID | O43745 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CHP2/IF_images/A-549_1.jpg|A-549]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CHP2/IF_images/HeLa_1.jpg|HeLa]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | Nucleus; Cytoplasm; Cell membrane |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 196 aa / 22.5 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 40 | PubMed 46 篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.5，PDB: 2BEC |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051875 - Calcineurin_B_homologous; InterPro: IP |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners, IntAct 10 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
|  | **原始总分** |  | **106/183** | **103.0/183** |  |  |  |
|  | **归一化总分** |  | **57.9/100** | **56.3/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus; Cytoplasm; Cell membrane | Swiss-Prot/TrEMBL |
| Protein Atlas (IF) | 暂无数据 | 暂无 HPA IF 数据 |

暂无数据（HPA IF 图像已本地嵌入。


**结论**: 核定位信号较弱，HPA 暂无 HPA IF 数据。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 46 |
| 研究方向 | 待补充关键文献摘要 |

**评价**: 非常新颖，仅有少数基础研究。

**关键文献**:
1. Śliwa-Dominiak J et al. (2013). "Chlamydia bacteriophages". *Arch Microbiol*. PMID: 23903989
2. Zhao X et al. (2018). "CHP2 Promotes Cell Proliferation in Breast Cancer via Suppression of FOXO3a". *Mol Cancer Res*. PMID: 29967111
3. Cai B et al. (2019). "Composition characterization of oyster polysaccharides from Crassostrea hongkongensis and their protective effect against H(2)O(2)-induced oxidative damage in IEC-6 cells". *Int J Biol Macromol*. PMID: 30452991
4. Oya T et al. (2025). "Characterization of the Swi6/HP1 binding motif in its partner protein reveals the basis for the functional divergence of the HP1 family proteins in fission yeast". *FASEB J*. PMID: 39945308
5. Lu B et al. (2020). "[The malignant phenotype of calcineurin B homologous protein 2 in gastric cancer and its clinical significance]". *Zhonghua Yi Xue Za Zhi*. PMID: 33342147
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.5 |
| 高置信度残基 (pLDDT>90) 占比 | 62.2% |
| 置信残基 (pLDDT 70-90) 占比 | 28.1% |
| 有序区域 (pLDDT>70) 占比 | 90.3% |
| 可用 PDB 条目 | 2BEC |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CHP2/CHP2-PAE.png]]

**评价**: AlphaFold 高质量预测（pLDDT=86.5，有序区 90.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051875 - Calcineurin_B_homologous; InterPro: IPR011992 - EF-hand-dom_pair; InterPro: IPR018247 - EF_Hand_1_ |

**染色质调控潜力分析**: 含明确的核酸结合/染色质相关结构域，多库确认。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| SLC9A1 | 0.981 | — | — |
| CLCA1 | 0.792 | — | — |
| ZG16 | 0.491 | — | — |
| PAPOLB | 0.466 | — | — |
| FKBP1A | 0.444 | — | — |
| FKBP1C | 0.444 | — | — |
| FKBP1B | 0.444 | — | — |
| FKBP3 | 0.444 | — | — |
| CASK | 0.439 | — | — |
| PPP3CA | 0.423 | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-8525536|ensembl:ENSP00000300113.2|intact:MINT-2729920|uniprotkb:A8K2I8 | — | — | — | — |
| intact:EBI-12267154|uniprotkb:A0PJM4|uniprotkb:A6NMF7|uniprotkb:F5H645|uniprotkb:Q66VZ3|uniprotkb:Q6DK36|uniprotkb:Q6IS86|uniprotkb:Q6ISA4|ensembl:ENSP00000430241.1 | — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 注释

**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 11
- 仅 IntAct 实验: 10
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.5 + PDB: 2BEC | pLDDT=86.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cell membrane | 待确认 |
| PPI | STRING + IntAct | 11 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CHP2 — Calcineurin B homologous protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小196 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 46 篇，研究基础有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新 5 篇关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43745
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CHP2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[CHP2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CHP2/CHP2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43745 |
| SMART | SM00054; |
| UniProt Domain [FT] | DOMAIN 26..61; /note="EF-hand 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 71..106; /note="EF-hand 2"; /evidence="ECO:0000305"; DOMAIN 111..146; /note="EF-hand 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 152..187; /note="EF-hand 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448" |
| InterPro | IPR051875;IPR011992;IPR018247;IPR002048; |
| Pfam | PF13202;PF13499; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166869-CHP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SLC9A1 | Intact, Biogrid | true |
| MDFI | Intact | false |
| SLC9A2 | Biogrid | false |
| SLC9A3 | Biogrid | false |
| SLC9A5 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
