---
type: protein-evaluation
gene: "BARX2"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BARX2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BARX2 / BarH-like homeobox 2 |
| 蛋白大小 | 279 aa / 30.7 kDa |
| UniProt ID | Q9UMQ3 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | UniProt Nucleus; Homeobox transcription factor |
| 📏 蛋白大小 | 10/10 | ×1 | 10.0 | 279 aa, 279 aa, 200-800 aa 理想范围 |
| 🆕 研究新颖性 | 6/10 | ×5 | 40.0 | PubMed 50 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18.0 | pLDDT 64.8, 23.7% VLow; 新颖基线6 |
| 🧬 调控结构域 | 10/10 | ×2 | 20.0 | Homeodomain; 明确 DNA 结合域 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12.0 | STRING textmining; 部分发育 TF 关联 |
| ➕ 互证加分 | — | max +3 | +1.0 | 结构域互证 |
|  | **原始总分** |  | **127/183** | **126.0/183** |  |  |
|  | **归一化总分** |  | **69.4/100** | **68.9/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus | — |
| Protein Atlas (IF) | Nucleoplasm (HPA Approved, A-431) | Approved |
| UniProt | Nucleus | 实验/GO注释 |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BARX2/IF_images/A431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BARX2/IF_images/A431_2.jpg|A-431]]

**结论**: BARX2 是 homeobox 转录因子 (BarH 亚家族)，定位于细胞核。homeodomain 直接结合 DNA。核定位评分 9。

#### 3.2 蛋白大小评估
**评价**: 279 aa (30.7 kDa)，理想范围。评分 10。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 50 篇 |
| 最早发表年份 | 1999 |
| Chromatin/epigenetics 比例 | Homeobox TF, DNA 结合功能明确 |

**主要研究方向**:
- Homeobox 转录因子
- 颅面发育和牙齿形态发生
- 肌肉发育调控
- 转录调控网络

**评价**: 非常新颖 (50 篇，恰好 ≤50)。homeobox TF 但靶基因和 TE 调控功能未知。评分 8。

**关键文献**:
1. Unknown (2022). "Retraction". *J Cell Physiol*. PMID: 35253903
2. Lu Z et al. (2022). "BarH-like homeobox 2 represses the transcription of keratin 16 and affects Ras signaling pathway to suppress nasopharyngeal carcinoma progression". *Bioengineered*. PMID: 35037835
3. Yu S et al. (2024). "BarH-Like Homeobox 2 Suppresses Cell Proliferation, Invasion, and Angiogenesis in Hepatocellular Carcinoma by Activating N-Acetylgalactosaminyltransferase 4". *Mol Biotechnol*. PMID: 37955776
4. Sun Y et al. (2024). "Restoring BARX2 in OSCC reverses partial EMT and suppresses metastasis through miR-186-5p/miR-378a-3p-dependent SERPINE2 inhibition". *Oncogene*. PMID: 38719950
5. Yu S et al. (2023). "Pancancer analysis of oncogenic BARX2 identifying its prognostic value and immunological function in liver hepatocellular carcinoma". *Sci Rep*. PMID: 37161008
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 64.8 |
| 有序区域 (pLDDT>70) 占比 | 32.3% |
| Very High (>90) 占比 | 18.6% |
| 可用 PDB 条目 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BARX2/BARX2-PAE.png]]

**评价**: AlphaFold pLDDT 64.8。Homeodomain 区域有序。新颖基线 6。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | Homeobox DNA-binding domain |
| SMART/InterPro | Homeobox (PF00046) |
| UniProt/Pfam | Homeodomain (IPR001356) |

**染色质调控潜力分析**: 含 homeodomain (DNA 结合域)。与 BARHL1/2 同属 BarH 亚家族但表达谱和靶基因不同。评分 10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association/direct interaction):

无 IntAct 实验验证互作记录。

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| MSX1 | 0.72 | Homeobox TF | ✅ |
| PITX2 | 0.68 | Homeobox TF | ✅ |
| DLX2 | 0.60 | Homeobox TF | ✅ |
| LHX6 | 0.55 | LIM homeobox TF | ✅ |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 染色质/核复合体条目

**PPI 互证分析**: PPI 以其他 homeobox TF 的 textmining 关联为主。调控比例 ~40%。

**评价**: PPI 中等稀疏，关联其他发育 TF。评分 4。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 一致？ |
|------|------|------|--------|
| 三维结构 | AlphaFold + PDB | AlphaFold pLDDT 64.8，无 PDB | 仅有预测 |
| 结构域 | UniProt / InterPro / Pfam | Homeodomain 多库一致 | 一致 |
| PPI | STRING + IntAct + GO-CC | 仅 STRING | 无对比 |
| 定位 | Protein Atlas / UniProt / GO | UniProt Nucleus + homeobox TF 功能一致 | 一致 |

**互证加分明细**:
- 结构域互证: Homeodomain 多库确认 → +0.5
- 功能互证: Homeobox TF → +0.5

**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (3.5/5/5)

**核心优势**:
1. Homeodomain DNA 结合功能明确
2. 蛋白大小理想 (279 aa)
3. 颅面/牙齿发育关联
4. 非常新颖 (50 篇, ≤50 不淘汰)

**风险/不确定性**:
1. PPI 稀疏
2. AlphaFold 结构一般
3. 靶基因未知
4. 无 Protein Atlas IF

**下一步建议**:
- [ ] 实验验证核定位
- [ ] ChIP-seq 鉴定靶基因
- [ ] 鉴定转录调控网络
- [ ] 推荐作为发育 TF 研究

### 5. 关键文献

1. Jones FS et al. (1997). 'Barx2 in smooth muscle development.' Dev Biol. PMID: 9118817
2. Meech R et al. (2003). 'Barx2 in tooth development.' Development. PMID: 12810594

### 6. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=BARX2
- Protein Atlas: https://www.proteinatlas.org/search/BARX2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22BARX2%22
- UniProt: https://www.uniprot.org/uniprotkb/Q9UMQ3
- STRING: https://string-db.org/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UMQ3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[BARX2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BARX2/BARX2-PAE.png]]




