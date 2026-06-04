---
type: protein-evaluation
gene: "KLHL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLHL2 |
| 蛋白名称 | Kelch-like protein 2 |
| 蛋白大小 | 593 aa / 66.0 kDa |
| UniProt ID | O95198 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Cytoplasm, cytoskeleton; Cell projection, ruffle; Cell proje |
| 蛋白大小 | 10/10 | ×1 | 10 | 593 aa / 66.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=92.3; PDB: 2XN4, 4CHB |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011705, IPR017096, IPR000210, IPR015915, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Uncertain |
| UniProt | Cytoplasm, cytoskeleton; Cell projection, ruffle; Cell projection; Cell projection, lamellipodium; C... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- lamellipodium (GO:0030027)
- ruffle (GO:0001726)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. KLHL2 interacts with and ubiquitinates WNK kinases.. *Biochemical and biophysical research communications*. PMID: 23838290
2. Ubiquitin ligase KLHL2 promotes the degradation and ubiquitination of ARHGEF7 protein to suppress renal cell carcinoma progression.. *American journal of cancer research*. PMID: 33163274
3. Kelch-Like Protein 2 Mediates Angiotensin II-With No Lysine 3 Signaling in the Regulation of Vascular Tonus.. *Journal of the American Society of Nephrology : JASN*. PMID: 25556166
4. Structural and biochemical characterization of the KLHL3-WNK kinase interaction important in blood pressure regulation.. *The Biochemical journal*. PMID: 24641320
5. Spatial and temporal expression patterns of genes around nine neuroticism-associated loci.. *Progress in neuro-psychopharmacology & biological psychiatry*. PMID: 28433457

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.3 |
| 高置信度残基 (pLDDT>90) 占比 | 85.0% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 4.6% |
| 有序区域 (pLDDT>70) 占比 | 94.1% |
| 可用 PDB 条目 | 2XN4, 4CHB |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2XN4, 4CHB）+ AlphaFold高质量预测（pLDDT=92.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR017096, IPR000210, IPR015915, IPR006652; Pfam: PF07707, PF00651, PF01344 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.991 | 0.639 | — |
| KLHL3 | 0.945 | 0.691 | — |
| KLHL12 | 0.929 | 0.734 | — |
| KEAP1 | 0.901 | 0.622 | — |
| WNK4 | 0.883 | 0.624 | — |
| KLHL9 | 0.801 | 0.065 | — |
| ENC1 | 0.799 | 0.000 | — |
| KLHL13 | 0.797 | 0.065 | — |
| SPOPL | 0.796 | 0.082 | — |
| RBX1 | 0.795 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000226725.6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| KLHL12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Dctn2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| csgG | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| TNPO2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| ZNF114 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TXNDC12 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TMA16 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.3 + PDB: 2XN4, 4CHB | pLDDT=92.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cell projection, ruffle;  / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KLHL2 — Kelch-like protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小593 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95198
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109466-KLHL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95198
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
