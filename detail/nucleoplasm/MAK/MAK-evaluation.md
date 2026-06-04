---
type: protein-evaluation
gene: "MAK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MAK — REJECTED (研究热度过高 (PubMed strict=250，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAK |
| 蛋白名称 | Serine/threonine-protein kinase MAK |
| 蛋白大小 | 623 aa / 70.6 kDa |
| UniProt ID | P20794 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Basal body, Cytosol, Connecting piece; 额外: Nucl; UniProt: Nucleus; Cytoplasm, cytoskeleton, microtubule organizing cen |
| 蛋白大小 | 10/10 | ×1 | 10 | 623 aa / 70.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=250 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR050117, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Basal body, Cytosol, Connecting piece; 额外: Nucleoli, Plasma membrane, Principal piece, End piece | Approved |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axoneme (GO:0005930)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- midbody (GO:0030496)
- mitotic spindle (GO:0072686)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 250 |
| PubMed broad count | 17115 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Nonsyndromic Retinitis Pigmentosa Overview.. **. PMID: 20301590
2. Regulation of Chondrocyte Metabolism and Osteoarthritis Development by Sirt5 Through Protein Lysine Malonylation.. *Arthritis & rheumatology (Hoboken, N.J.)*. PMID: 40176311
3. Chlamydomonas protein kinase MAK phosphorylates FAP256/CEP104 and regulates axonemal microtubule assembly.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 41231942
4. MAPK/MAK/MRK overlapping kinase (MOK) controls microglial inflammatory/type-I IFN responses via Brd4 and is involved in ALS.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37399380
5. Ccrk-Mak/Ick signaling is a ciliary transport regulator essential for retinal photoreceptor survival.. *Life science alliance*. PMID: 39293864

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.1 |
| 高置信度残基 (pLDDT>90) 占比 | 35.5% |
| 置信残基 (pLDDT 70-90) 占比 | 8.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 52.0% |
| 有序区域 (pLDDT>70) 占比 | 44.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.1），有序残基占 44.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR050117, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCM3 | 0.801 | 0.801 | — |
| CDC6 | 0.787 | 0.782 | — |
| MCM2 | 0.787 | 0.782 | — |
| ORC4 | 0.783 | 0.782 | — |
| ORC3 | 0.783 | 0.782 | — |
| MCM7 | 0.782 | 0.782 | — |
| MCM6 | 0.782 | 0.782 | — |
| ORC2 | 0.782 | 0.782 | — |
| CDT1 | 0.782 | 0.782 | — |
| MCM5 | 0.782 | 0.782 | — |

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
| 三维结构 | AlphaFold pLDDT=62.1 + PDB: 无 | pLDDT=62.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, microtubule orga / Nucleoplasm, Basal body, Cytosol, Connecting piece | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MAK — Serine/threonine-protein kinase MAK，研究基础较多，新颖性有限。
2. 蛋白大小623 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 250 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 250 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P20794
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111837-MAK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P20794
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
