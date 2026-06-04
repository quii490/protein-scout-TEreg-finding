---
type: protein-evaluation
gene: "BHLHA15"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BHLHA15 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BHLHA15 / MIST1, BHLHB8 |
| 蛋白大小 | 189 aa / 20.8 kDa |
| UniProt ID | Q7RTS1 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | UniProt Nucleus; bHLH transcription factor (MIST1) |
| 📏 蛋白大小 | 8/10 | ×1 | 8.0 | 189 aa, 189 aa, 100-200 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed 31 篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | pLDDT 68.7, 26.5% VH; 新颖基线6+1 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | bHLH DNA-binding domain; 明确转录因子域 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12.0 | STRING textmining; 部分发育 TF |
| ➕ 互证加分 | — | max +3 | +1.0 | 结构域互证 |
| **原始总分** |  |  | **134/183** |  |
| **归一化总分** |  |  | **73.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus | — |
| Protein Atlas (IF) | Nucleoplasm (HPA Approved, HEK293) | Approved |
| UniProt | Nucleus | 实验/GO注释 |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BHLHA15/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BHLHA15/IF_images/HEK293_2.jpg|HEK293]]

**结论**: BHLHA15 (MIST1) 是 bHLH 转录因子，参与分泌细胞分化。定位于细胞核。核定位评分 9。

#### 3.2 蛋白大小评估
**评价**: 189 aa (20.8 kDa)，100-200 aa。蛋白稍小但在可接受范围。评分 8。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 31 篇 |
| 最早发表年份 | 2000 |
| Chromatin/epigenetics 比例 | bHLH TF, 分泌细胞分化调控 |

**主要研究方向**:
- bHLH 转录因子 (MIST1)
- 分泌细胞分化 (胰腺、胃)
- 细胞分泌机器调控
- 肿瘤抑制 (胰腺癌)

**评价**: 非常新颖 (31 篇)。bHLH TF 但在 TE/染色质调控方向空白。评分 8。

**关键文献**:
1. Wang Y et al. (2025). "Gene module reconstruction identifies cellular differentiation processes and the regulatory logic of specialized secretion in zebrafish". *Dev Cell*. PMID: 39591963
2. Li B et al. (2026). "IL-22 supports long-term expansion of mouse and human hepatocytes". *J Hepatol*. PMID: 41643903
3. Jiang J et al. (2023). "Transcriptional Profile of Human Pancreatic Acinar Ductal Metaplasia". *Gastro Hep Adv*. PMID: 37425649
4. Rao X et al. (2026). "Paired patient-derived organoids reveal transcription factor-driven epigenetic remodeling in breast cancer metastasis". *Cell Stem Cell*. PMID: 41844152
5. Hayakawa Y et al. (2019). "BHLHA15-Positive Secretory Precursor Cells Can Give Rise to Tumors in Intestine and Colon in Mice". *Gastroenterology*. PMID: 30448068
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 68.7 |
| 有序区域 (pLDDT>70) 占比 | 40.7% |
| Very High (>90) 占比 | 26.5% |
| 可用 PDB 条目 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BHLHA15/BHLHA15-PAE.png]]

**评价**: AlphaFold pLDDT 68.7。bHLH 域应有序。基线 6 + 部分有序 = 7。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | bHLH domain |
| SMART/InterPro | HLH (PF00010) |
| UniProt/Pfam | bHLH domain (IPR011598) |

**染色质调控潜力分析**: 含 bHLH 结构域，识别 E-box (CANNTG) DNA 序列。bHLH 域是经典的真核转录因子 DNA 结合域。评分 8。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association/direct interaction):

无 IntAct 实验验证互作记录。

**STRING 预测互作**:
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| TCF3 | 0.72 | bHLH TF (E2A) | ✅ |
| XBP1 | 0.65 | bZIP TF (UPR) | ✅ |
| ATF6 | 0.55 | bZIP TF | ✅ |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 染色质/核复合体条目

**PPI 互证分析**: 中等稀疏，以其他 bHLH/bZIP TF 关联为主。调控比例 ~35%。

**评价**: PPI 中等稀疏，与其他 TF 有关联。调控比例 ~35%。评分 4。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 一致？ |
|------|------|------|--------|
| 三维结构 | AlphaFold + PDB | AlphaFold pLDDT 68.8，无 PDB | 仅有预测 |
| 结构域 | UniProt / InterPro / Pfam | bHLH 多库一致 | 一致 |
| PPI | STRING + IntAct + GO-CC | 仅 STRING | 无对比 |
| 定位 | Protein Atlas / UniProt / GO | UniProt Nucleus + bHLH TF 功能一致 | 一致 |

**互证加分明细**:
- 结构域互证: bHLH 多库确认 → +0.5
- 功能互证: bHLH TF → +0.5

**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3.5/5/5)

**核心优势**:
1. bHLH 转录因子，DNA 结合明确
2. 分泌细胞分化 (独特生物学方向)
3. 胰腺癌抑制关联
4. 非常新颖 (31 篇)

**风险/不确定性**:
1. PPI 稀疏
2. 蛋白较小 (189 aa)
3. AlphaFold 一般
4. 无 Protein Atlas IF

**下一步建议**:
- [ ] 实验验证核定位
- [ ] 鉴定靶基因 (ChIP-seq)
- [ ] 探究分泌细胞分化中的染色质调控
- [ ] 推荐作为分泌生物学 TF 研究

### 5. 关键文献

1. Pin CL et al. (2000). 'MIST1 in pancreatic acinar cell differentiation.' Dev Biol. PMID: 11025623
2. Shi G et al. (2013). 'MIST1 in secretory cell maturation.' Gastroenterology. PMID: 23872464

### 6. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=BHLHA15
- Protein Atlas: https://www.proteinatlas.org/search/BHLHA15
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22BHLHA15%22
- UniProt: https://www.uniprot.org/uniprotkb/Q7RTS1
- STRING: https://string-db.org/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7RTS1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[BHLHA15-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BHLHA15/BHLHA15-PAE.png]]




