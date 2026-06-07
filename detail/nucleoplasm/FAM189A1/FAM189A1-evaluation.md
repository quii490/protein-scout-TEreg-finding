---
type: protein-evaluation
gene: "FAM189A1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM189A1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM189A1 / FAM189A1, KIAA0574, TMEM228 |
| 蛋白名称 | Protein ENTREP2 |
| 蛋白大小 | 539 aa / 56.5 kDa |
| UniProt ID | O60320 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM189A1/IF_images/U-251MG_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM189A1/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Vesicles, Aggresome; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 539 aa / 56.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007237, IPR030431; Pfam: PF04103 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Aggresome | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM189A1, KIAA0574, TMEM228 |

**关键文献**:
1. Aberrations in sperm DNA methylation patterns of males suffering from reduced fecundity.. *Andrologia*. PMID: 29072328
2. FAM189A2 activates Hippo signaling pathway by abrogating WWP2-mediated LATS1 ubiquitination, to inhibit the glycolysis and proliferation processes of lung adenocarcinoma.. *Journal of translational medicine*. PMID: 41350729
3. Overlapping pathogenic de novo CNVs in neurodevelopmental disorders and congenital anomalies impacting constraint genes regulating early development.. *Human genetics*. PMID: 36383254
4. Hypomethylation and Genetic Instability in Monosomy Blastocysts May Contribute to Decreased Implantation Potential.. *PloS one*. PMID: 27434648
5. RNA-seq Reveals Transcriptomic Differences in Inflamed and Noninflamed Intestinal Mucosa of Crohn's Disease Patients Compared with Normal Mucosa of Healthy Controls.. *Inflammatory bowel diseases*. PMID: 28613228

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.0 |
| 高置信度残基 (pLDDT>90) 占比 | 8.9% |
| 置信残基 (pLDDT 70-90) 占比 | 23.9% |
| 中等置信 (pLDDT 50-70) 占比 | 23.2% |
| 低置信 (pLDDT<50) 占比 | 44.0% |
| 有序区域 (pLDDT>70) 占比 | 32.8% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM189A1/FAM189A1-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=59.0），有序残基占 32.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007237, IPR030431; Pfam: PF04103 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IQCA1L | 0.605 | 0.000 | — |
| TMEM88B | 0.488 | 0.000 | — |
| TMEM179 | 0.478 | 0.000 | — |
| APBA2 | 0.474 | 0.000 | — |
| TMEM145 | 0.460 | 0.000 | — |
| STUM | 0.454 | 0.000 | — |
| FAM81A | 0.451 | 0.000 | — |
| FAM171B | 0.449 | 0.000 | — |
| TMEM59L | 0.436 | 0.042 | — |
| AMER3 | 0.434 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.0 + PDB: 无 | pLDDT=59.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Vesicles, Aggresome | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM189A1 — Protein ENTREP2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小539 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60320
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104059-ENTREP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM189A1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60320
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM189A1/FAM189A1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60320 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007237;IPR030431; |
| Pfam | PF04103; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000104059-ENTREP2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
