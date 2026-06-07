---
type: protein-evaluation
gene: "CENPI"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CENPI 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPI / Centromere protein I |
| 蛋白大小 | 756 aa / 86.7 kDa |
| UniProt ID | Q92674 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPI/IF_images/SiHa_1.jpg|SiHa]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPI/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | Nucleus; Chromosome, centromere |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 756 aa / 86.7 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 54 篇 |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.8，PDB: 7PB4, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO, 7YWX, 7YYH |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012485 - CENP-I; Pfam: PF07778 - CENP-I |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 20 partners, IntAct 37 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** |  |  | **132/183** |  |
| **归一化总分** |  |  | **72.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus; Chromosome, centromere | Swiss-Prot/TrEMBL |
| Protein Atlas (IF) | 暂无数据 | 暂无 HPA IF 数据 |

暂无数据（HPA IF 图像已本地嵌入。


**结论**: 主要定位于细胞核，HPA 暂无 HPA IF 数据。

#### 3.2 蛋白大小评估

**评价**: 大小适中，适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 54 |
| 研究方向 | 待补充关键文献摘要 |

**评价**: 有一定研究基础，但仍存在未探索的niche空间。

**关键文献**:
1. Wu C et al. (2025). "Centromere protein I facilitates breast cancer tumorigenesis and disease progression through modulation of Wnt/β-Catenin signaling". *Cancer Cell Int*. PMID: 41074145
2. Bao X et al. (2025). "Bioinformatics Combined With Biological Experiments to Identify the Pathogenetic Link of Type 2 Diabetes for Breast Cancer". *Cancer Med*. PMID: 40202151
3. He R et al. (2025). "Centromere Protein I, a Cell Cycle Checkpoint Gene, Accelerates Tumor Progression via the Hippo Pathway and Mediates Immune Escape in Hepatocellular Carcinoma". *J Clin Transl Hepatol*. PMID: 41473255
4. Liu D et al. (2026). "Centromere protein I promotes hepatocellular carcinoma progression by activating PI3K/AKT/mTOR-CDK2 cascade". *Cancer Biol Ther*. PMID: 42124320
5. Feng Z et al. (2024). "Immune infiltration related CENPI associates with the malignant features and drug resistance of lung adenocarcinoma". *Biochim Biophys Acta Mol Basis Dis*. PMID: 38232915
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 22.1% |
| 置信残基 (pLDDT 70-90) 占比 | 47.6% |
| 有序区域 (pLDDT>70) 占比 | 69.7% |
| 可用 PDB 条目 | 7PB4, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO, 7YWX, 7YYH |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPI/CENPI-PAE.png]]

**评价**: PDB 实验结构（7PB4, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO, 7YWX, 7YYH）+ AlphaFold 高质量预测（pLDDT=73.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012485 - CENP-I; Pfam: PF07778 - CENP-I |

**染色质调控潜力分析**: 存在注释结构域：InterPro: IPR012485 - CENP-I; Pfam: PF07778 - CENP-I...。新颖蛋白基线不扣分。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CENPT | 0.999 | — | — |
| CENPN | 0.999 | — | — |
| CENPL | 0.999 | — | — |
| CENPM | 0.999 | — | — |
| CENPA | 0.999 | — | — |
| CENPP | 0.999 | — | — |
| CENPO | 0.999 | — | — |
| CENPQ | 0.999 | — | — |
| CENPH | 0.999 | — | — |
| CENPU | 0.999 | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-1003677|ensembl:ENSGALP00010014558.1 | — | — | — | — |
| intact:EBI-11085153|ensembl:ENSP00000362018.1|ensembl:ENSP00000507595.1|ensembl:ENSP00000507927.1|uniprotkb:Q96ED0|uniprotkb:Q5JWZ9 | — | — | — | — |
| intact:EBI-2561019|uniprotkb:Q8TB66|uniprotkb:A8K788|uniprotkb:Q96ED4|ensembl:ENSP00000285814.4 | — | — | — | — |
| intact:EBI-10980537|ensembl:ENSP00000384726.1 | — | — | — | — |
| intact:EBI-2954772|uniprotkb:Q8N2Z8|uniprotkb:Q9H5A1|uniprotkb:A8K8J7|ensembl:ENSP00000386226.3 | — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 注释

**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 20
- 仅 IntAct 实验: 37
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 20 个预测互作，IntAct 37 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 7PB4, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO, 7YWX, 7YYH | pLDDT=73.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere | 待确认 |
| PPI | STRING + IntAct | 20 + 37 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CENPI — Centromere protein I，有一定研究基础，但仍存在未探索的niche空间。
2. 蛋白大小756 aa，大小适中，适合常规生化实验和结构解析。

**风险/不确定性**:
1. 已有一定研究，需确认独特研究角度
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新 5 篇关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92674
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPI
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CENPI


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[CENPI-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPI/CENPI-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92674 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012485; |
| Pfam | PF07778; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000102384-CENPI/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CENPH | Biogrid, Bioplex | true |
| CENPK | Intact, Biogrid | true |
| CENPM | Biogrid, Opencell | true |
| CENPA | Biogrid | false |
| CENPN | Biogrid | false |
| CENPO | Biogrid | false |
| CENPQ | Biogrid | false |
| CENPU | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
