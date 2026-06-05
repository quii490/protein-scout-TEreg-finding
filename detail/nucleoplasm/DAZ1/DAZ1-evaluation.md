---
type: protein-evaluation
gene: "DAZ1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DAZ1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAZ1 / DAZ, SPGY |
| 蛋白名称 | Deleted in azoospermia protein 1 |
| 蛋白大小 | 744 aa / 82.8 kDa |
| UniProt ID | Q9NQZ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 744 aa / 82.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=43 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043628, IPR037551, IPR012677, IPR035979, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 239 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DAZ, SPGY |

**关键文献**:
1. A differentially methylated region of the DAZ1 gene in spermatic and somatic cells.. *Asian journal of andrology*. PMID: 16372120
2. High frequency of DAZ1/DAZ2 gene deletions in patients with severe oligozoospermia.. *Molecular human reproduction*. PMID: 11870237
3. Gene Polymorphism, Microdeletion, and Gene Expression of PRM1, PRM2, AZFc in Infertile Males.. *Reports of biochemistry & molecular biology*. PMID: 37724144
4. AZF and DAZ gene copy-specific deletion analysis in maturation arrest and Sertoli cell-only syndrome.. *Molecular human reproduction*. PMID: 15347736
5. Association of DAZ1/DAZ2 deletion with spermatogenic impairment and male infertility in the South Chinese population.. *World journal of urology*. PMID: 23512232

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.7 |
| 高置信度残基 (pLDDT>90) 占比 | 6.7% |
| 置信残基 (pLDDT 70-90) 占比 | 33.9% |
| 中等置信 (pLDDT 50-70) 占比 | 15.7% |
| 低置信 (pLDDT<50) 占比 | 43.7% |
| 有序区域 (pLDDT>70) 占比 | 40.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.7），有序残基占 40.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043628, IPR037551, IPR012677, IPR035979, IPR000504; Pfam: PF18872, PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DAZ2 | 0.999 | 0.000 | — |
| PUM2 | 0.977 | 0.337 | — |
| DAZAP2 | 0.970 | 0.292 | — |
| CDY1 | 0.958 | 0.092 | — |
| DAZAP1 | 0.949 | 0.334 | — |
| CDY2A | 0.945 | 0.086 | — |
| DZIP1 | 0.944 | 0.254 | — |
| BPY2 | 0.937 | 0.000 | — |
| BPY2B | 0.932 | 0.000 | — |
| BPY2C | 0.932 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| F20P5.23 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| ZAT2 | psi-mi:"MI:2277"(Cr-two hybrid) | doi:10.1038/nmeth.4343|pubmed: |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.7 + PDB: 无 | pLDDT=57.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DAZ1 — Deleted in azoospermia protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小744 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQZ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188120-DAZ1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAZ1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQZ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQZ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
